import logging
import secrets
import sys

import boto3
import jwt
from boto3 import Session

from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from rest_framework import status
from rest_framework.response import Response


from environment.main import (JWT_SECRET_KEY, JWT_ALGORITHM
, AWS_MEDIA_FOLDER, AWS_ACCESS_KEY_ID, SENTIMENT_KEYWORDS, MIN_CONFIDENCE)
from environment.main import (
    AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME, AWS_MEDIA_FOLDER,
    AWS_S3_BASE_URL
)
# from user.models import EmailTemplate, User
from validators.Errorcode import ErrorCode
from validators.Errormessage import ErrorMessage
from django.core.paginator import Paginator
from .constants import PAGINATION_COUNT, AGENT, PARTNER, CONSUMER
from datetime import datetime, timedelta, date, time
from django.utils import timezone
from django.contrib.auth.tokens import default_token_generator as token_generator
import django_filters


from django.conf import settings
import pgeocode

logger = logging.getLogger(__name__)

class CommonUtils(object):

    @staticmethod
    def dispatch_success(request, response, code=status.HTTP_200_OK):
        """
        :param request: request object
        :param response: response object
        :param code: 200 - success code
        :return: json object
        """

        response = {"status": "success", "result": response}

        # logging the success response..
        extras = {
            "status": "Success",
            "url": request.get_full_path(),
            "log_message": "Request completed!",
            "method": request.method,
            "user": request.user
        }
        logger = logging.getLogger('success')
        logger.setLevel(logging.INFO)
        logger.info("Success: ", extra=extras)

        return Response(response, status=code)

    @staticmethod
    def dispatch_failure(request, identifier, response=None, code=status.HTTP_400_BAD_REQUEST, message_params=None):
        """
        @param request: request object
        @param identifier: error identifier code
        @param response: response object may be empty in some cases
        @param code: 400 - Failure
        @param message_params: To add in error message
        :return: json object
        """
        logger = logging.getLogger('failure')
        logger.setLevel(logging.DEBUG)
        try:
            if hasattr(ErrorCode, identifier):
                error_code = getattr(ErrorCode, identifier)
            else:
                error_code = code
            error_message = getattr(ErrorMessage, identifier)
            if error_message and message_params:
                error_message = error_message.format(**message_params)
            errors = {}
            if response is None:
                errors['status'] = 'failed'
                errors['code'] = error_code
                errors['message'] = error_message
            else:
                errors['status'] = 'failed'
                errors['code'] = error_code
                errors['message'] = error_message
                errors['errors'] = response

            response = Response(data=errors, status=code)

            # logging the failure response
            extras = {
                "request_data": request.data,
                "response_data": str(response.data),
                "status": "Failed",
                "url": request.get_full_path(),
                "log_message": error_message,
                "method": request.method,
                "user": request.user,
                "file_name": '',
                "line_no": ''
            }
            exception_type, exception_object, exception_traceback = sys.exc_info()
            if exception_type and exception_object and exception_traceback:
                extras["file_name"] = exception_traceback.tb_frame.f_code.co_filename
                extras["line_no"] = exception_traceback.tb_lineno

            logger.debug("Error: ", extra=extras)
            return response
        except Exception as e:
           logger.exception("An error occurred") 

    @staticmethod
    def info_logger(message, request=None):
        extras = {
            "request_data": "",
            "response_data": "",
            "status": "Info",
            "url": "",
            "log_message": message,
            "method": "",
            "user": ""
        }
        if request:
            extras["request_data"] = request.data
            extras["method"] = request.method
            extras["user"] = request.user

        logger = logging.getLogger('success')
        logger.setLevel(logging.INFO)
        logger.info("Info: ", extra=extras)



    @staticmethod
    def get_paginated(query_set, serializer, current_page, per_page=PAGINATION_COUNT, order_by=None, context=None):
        """
        This method paginates the provided query set based on
        requested page and returns the paginated response body
        @param query_set: Queryset object of a model
        @param serializer: Serializer to use on query set
        @param current_page: Requested Page
        @param per_page: Required records per page
        @param order_by: Sorting Field
        @param context: Context dictionary to pass into the serializer
        @return: Paginated response body
        """

        if order_by:
            query_set = query_set.order_by(order_by)
        total_count = query_set.count()  # Get the total number of records
        if total_count == 0:
            return {
                'page': current_page,
                'total_pages': 0,
                'total_count': 0,
                'records_per_page': per_page,
                'data': []
            }

        # Ensure per_page is valid
        per_page = min(per_page, total_count)  # Avoid exceeding total records
        paginator = Paginator(query_set, per_page)
        total_pages = paginator.num_pages

        try:
            current_page = max(1, int(current_page))  # Ensure page is at least 1
            page = paginator.page(current_page)
        except Exception:
            raise Exception('Page not found')

        result_data = page.object_list
        if serializer:
            serializer = serializer(page.object_list, many=True, context=context)
            result_data = serializer.data

        return {
            'page': current_page,
            'total_pages': total_pages,
            'total_count': total_count,
            'records_per_page': per_page,
            'data': result_data
        }

    @staticmethod
    def create_access(user):
        payload = {
            "user_id": user.id,
            "email": user.email,
            "username": user.username,
            "expired_at": int((datetime.utcnow() + timedelta(days=2)).timestamp())
        }
        token = jwt.encode(payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
        payload["access_token"] = token
        return payload

    @staticmethod
    def generate_verification_link(user):
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = token_generator.make_token(user)
        return settings.BACKEND_URL +f"/api/user/verify-account/{uid}/{token}/"

    @staticmethod
    def error_logger(message, request=None):
        extras = {
            "request_data": "",
            "response_data": "",
            "status": "Error",
            "url": "",
            "log_message": message,
            "method": "",
            "user": "",
            "file_name": '',
            "line_no": ''
        }
        exception_type, exception_object, exception_traceback = sys.exc_info()
        if exception_type and exception_object and exception_traceback:
            extras["file_name"] = exception_traceback.tb_frame.f_code.co_filename
            extras["line_no"] = exception_traceback.tb_lineno

        if request:
            extras["request_data"] = request.data
            extras["method"] = request.method
            extras["user"] = request.user

        logger = logging.getLogger('failure')
        logger.setLevel(logging.DEBUG)
        logger.debug("Error: ", extra=extras)

    @staticmethod
    def export_as_csv(data, headers, filename="export.csv"):
        """
        Export a list of dicts as a CSV file, upload to S3, and return a link.
        :param data: List of dicts (rows)
        :param headers: List of field names (columns)
        :param filename: Name of the file to download
        :return: DRF Response with S3 link
        """
        import csv
        from io import StringIO
        from rest_framework.response import Response

        output = StringIO()
        writer = csv.DictWriter(output, fieldnames=headers)
        writer.writeheader()
        for row in data:
            writer.writerow({h: row.get(h, "") for h in headers})
        csv_content = output.getvalue().encode("utf-8")
        # Generate S3 file path
        from .utils import FileUtils
        file_path = FileUtils.generate_file_path(
            name_template="export_{}_{}.{}",
            folder="exports",
            extension="csv"
        )
        s3_url = FileUtils.upload_file(csv_content, file_path, content_type="text/csv")
        if not s3_url:
            return Response({"error": "Failed to upload CSV to S3"}, status=500)
        return Response({"url": s3_url, "filename": filename})







class FileUtils:


    @staticmethod
    def generate_file_path(name_template, folder, extension='csv'):
        name = name_template.format(int(timezone.now().timestamp()), secrets.token_hex(2), extension)
        return f'{AWS_MEDIA_FOLDER}/{folder}/{name}'

    @staticmethod
    def get_bucket():
        aws_session = Session(
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_S3_REGION_NAME
        )
        s3 = aws_session.resource('s3')
        client = aws_session.client('s3')
        bucket = s3.Bucket(AWS_STORAGE_BUCKET_NAME)
        return client, bucket

    @staticmethod
    def upload_file(data, file_path, content_type):
        try:
            client, bucket = FileUtils.get_bucket()
            bucket.put_object(Key=file_path, Body=data, ContentType=content_type)
            return AWS_S3_BASE_URL + file_path
        except Exception as e:
            CommonUtils.error_logger(f'[FileUtils.upload_file]: Error: {e}')
            return None

    @staticmethod
    def download_file(file_path):
        try:
            client, bucket = FileUtils.get_bucket()
            response = client.get_object(Bucket=AWS_STORAGE_BUCKET_NAME, Key=file_path)
            return response.get('Body').read()
        except Exception as e:
            CommonUtils.error_logger(f'[FileUtils.download_file]: Error: {e}')
            return None

    @staticmethod
    def delete_file(file_key):
        try:
            client, bucket = FileUtils.get_bucket()
            client.delete_object(Bucket=AWS_STORAGE_BUCKET_NAME, Key=file_key)
            return True
        except Exception as e:
            CommonUtils.error_logger(f'[FileUtils.delete_file]: Error: {e}')
            return False


    @staticmethod
    def get_signed_url(file_path):
        try:
            client, _ = FileUtils.get_bucket()
            return client.generate_presigned_url(ClientMethod='get_object', Params={
                'Bucket': AWS_STORAGE_BUCKET_NAME, 'Key': file_path
            })
        except Exception as e:
            CommonUtils.error_logger(f'[FileUtils.download_file]: Error: {e}')
            return None

    @staticmethod
    def check_moderation(uploaded_file):
        """
        Checks moderation for sensitive content before the file gets uploaded.
        """
        try:
            content_type = uploaded_file.content_type

            if content_type.startswith("image/"):
                # Process image using Rekognition
                rekognition = boto3.client(
                    'rekognition',
                    region_name=AWS_S3_REGION_NAME,
                    aws_access_key_id = AWS_ACCESS_KEY_ID,
                    aws_secret_access_key = AWS_SECRET_ACCESS_KEY
                )
                response = rekognition.detect_moderation_labels(
                    Image={'Bytes': uploaded_file.read()},
                    MinConfidence=int(MIN_CONFIDENCE)
                )
                raw_labels = response.get("ModerationLabels", [])
                labels = [label["Name"] for label in raw_labels]
                is_safe = len(labels) == 0
                return {"is_safe": is_safe, "labels": labels}

            # elif content_type == "application/pdf":
            #     # Process PDF using Textract
            #     textract = boto3.client(
            #         'textract',
            #         region_name=AWS_S3_REGION_NAME,
            #         aws_access_key_id = AWS_ACCESS_KEY_ID,
            #         aws_secret_access_key = AWS_SECRET_ACCESS_KEY)
            #     response = textract.detect_document_text(
            #         Document={'Bytes': uploaded_file.read()}
            #     )
            #
            #     detected_text = " ".join(
            #         [block['Text'] for block in response.get('Blocks', []) if block['BlockType'] == 'LINE'])
            #
            #     # Basic text moderation (simple keyword scan)
            #     flagged_keywords = FLAGGED_KEYWORDS  # can be extended
            #     found_keywords = [word for word in flagged_keywords if word.lower() in detected_text.lower()]
            #
            #     is_safe = len(found_keywords) == 0
            #     return {"is_safe": is_safe, "labels": found_keywords}

            elif content_type == "application/pdf":
                # Process PDF using Textract
                textract = boto3.client(
                    'textract',
                    region_name=AWS_S3_REGION_NAME,
                    aws_access_key_id=AWS_ACCESS_KEY_ID,
                    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
                )
                response = textract.detect_document_text(
                    Document={'Bytes': uploaded_file.read()}
                )

                detected_text = " ".join(
                    [block['Text'] for block in response.get('Blocks', []) if block['BlockType'] == 'LINE']
                )

                # Analyze sentiment using Amazon Comprehend
                comprehend = boto3.client(
                    'comprehend',
                    region_name=AWS_S3_REGION_NAME,
                    aws_access_key_id=AWS_ACCESS_KEY_ID,
                    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
                )

                # Limit to 5000 characters
                short_text = detected_text[:5000]

                sentiment_response = comprehend.detect_sentiment(
                    Text=short_text,
                    LanguageCode='en'
                )

                sentiment = sentiment_response.get("Sentiment", "UNKNOWN")
                is_safe = sentiment not in SENTIMENT_KEYWORDS

                return {"is_safe": is_safe, "labels": [f"Sentiment: {sentiment}"]}

            else:
                return {"is_safe": True, "labels": []}

        except Exception as e:
            CommonUtils.error_logger(f"[FileUtils.check_moderation]: Error: {e}")
            return {"is_safe": False, "labels": ["Moderation error"]}



_NOMI = pgeocode.Nominatim("us")
EARTH_RADIUS_MI = 3959   # great-circle distance in miles


