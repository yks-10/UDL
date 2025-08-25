import jwt
from rest_framework.exceptions import APIException
from rest_framework.permissions import BasePermission, IsAuthenticated, IsAdminUser
from user.models import User, Blocklist
from environment.main import JWT_SECRET_KEY, JWT_ALGORITHM
from datetime import datetime, timedelta, date
from rest_framework import status
from validators.Errormessage import ErrorMessage
from validators.Errorcode import ErrorCode
from validators.Error import Error

class UnauthorizedAccess(APIException):
    """
    UnAuthorized Access Exception if access token is not provided or invalid
    """
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = {"status": "failed",
                      "code": ErrorCode.UNAUTHORIZED_ACCESS,
                      "message": ErrorMessage.UNAUTHORIZED_ACCESS}


class TokenExpired(APIException):
    """
    TokenExpired class to be raised when the JWT access token is expired
    """
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = {"status": "failed",
                      "code": ErrorCode.ACCESS_TOKEN_EXPIRED,
                      "message": ErrorMessage.ACCESS_TOKEN_EXPIRED}


class IsValidated(IsAuthenticated):
    def has_permission(self, request, view):
        """
        Access Token Validation using JWT
        It parses the token using the secret key
        if its an valid token will allow to access the apis or returns UnAuthorizedAccess (401)

        @param request: Http Request (Should contains HTTP_AUTHORIZATION header)
        @param view: Respective View that has been called
        @return: True if valid user
        """
        try:
            auth_token = request.META.get('HTTP_AUTHORIZATION')
            token = auth_token.split(' ')

            payload = jwt.decode(token[1], JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])

            # To check whether the token is expired or not
            if payload.get("expired_at") < int(datetime.utcnow().timestamp()):
                raise TokenExpired
            user = User.objects.get(pk=payload.get("user_id"), is_active=True)
            request.user = user

            return True
        except User.DoesNotExist:
            raise UnauthorizedAccess
        except TokenExpired:
            raise TokenExpired
        except Exception:
            raise UnauthorizedAccess


class IsAdmin(IsAuthenticated):
    def has_permission(self, request, view):
        try:
            auth_token = request.META.get('HTTP_AUTHORIZATION')
            token = auth_token.split(' ')

            payload = jwt.decode(token[1], JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])

            # To check whether the token is expired or not
            if payload.get("expired_at") < int(datetime.utcnow().timestamp()):
                raise TokenExpired
            user = User.objects.get(pk=payload.get("user_id"), is_active=True)
            request.user = user
            if user.user_type == 'admin':
                return True
            else:
                return False
        except User.DoesNotExist:
            raise UnauthorizedAccess
        except TokenExpired:
            raise TokenExpired
        except Exception:
            raise UnauthorizedAccess

class IsOfficer(IsAuthenticated):
    def has_permission(self, request, view):
        # return request.user.is_authenticated and request.user.user_type == 'partner'
        try:
            auth_token = request.META.get('HTTP_AUTHORIZATION')
            token = auth_token.split(' ')

            payload = jwt.decode(token[1], JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])

            # To check whether the token is expired or not
            if payload.get("expired_at") < int(datetime.utcnow().timestamp()):
                raise TokenExpired
            user = User.objects.get(pk=payload.get("user_id"), is_active=True)
            request.user = user
            if user.user_type == 'officer':
                return True
            else:
                return False
        except User.DoesNotExist:
            raise UnauthorizedAccess
        except TokenExpired:
            raise TokenExpired
        except Exception:
            raise UnauthorizedAccess

class IsPartner(IsAuthenticated):
    def has_permission(self, request, view):
        try:
            auth_token = request.META.get('HTTP_AUTHORIZATION')
            token = auth_token.split(' ')

            payload = jwt.decode(token[1], JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])

            # To check whether the token is expired or not
            if payload.get("expired_at") < int(datetime.utcnow().timestamp()):
                raise TokenExpired
            user = User.objects.get(pk=payload.get("user_id"), is_active=True)
            request.user = user
            if user.user_type == 'partner':
                return True
            else:
                return False
        except User.DoesNotExist:
            raise UnauthorizedAccess
        except TokenExpired:
            raise TokenExpired
        except Exception:
            raise UnauthorizedAccess


class OnlyAdmin(IsAuthenticated):
    def has_permission(self, request, view):
        """
        Should pass the username and password of the admin user in request data
        to access this resource
        @param request: Http Request
        @param view: Respective View that has been called
        @return: True if valid user
        """
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            if username and password:
                user = User.objects.get(username=username, is_staff=True, is_superuser=True)
                if user.check_password(password):
                    request.user = user
                    return True
            raise UnauthorizedAccess
        except User.DoesNotExist:
            raise UnauthorizedAccess
        except Exception:
            raise UnauthorizedAccess

class OfficerOrAdmin(IsAuthenticated):
    def has_permission(self, request, view):
        try:
            auth_token = request.META.get('HTTP_AUTHORIZATION')
            token = auth_token.split(' ')

            payload = jwt.decode(token[1], JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])

            # To check whether the token is expired or not
            if payload.get("expired_at") < int(datetime.utcnow().timestamp()):
                raise TokenExpired
            user = User.objects.get(pk=payload.get("user_id"), is_active=True)
            request.user = user
            if user.user_type in ['admin','officer'] :
                return True
            else:
                return False
        except User.DoesNotExist:
            raise UnauthorizedAccess
        except TokenExpired:
            raise TokenExpired
        except Exception:
            raise UnauthorizedAccess

class PartnerOrAdmin(IsAuthenticated):
    def has_permission(self, request, view):
        try:
            auth_token = request.META.get('HTTP_AUTHORIZATION')
            token = auth_token.split(' ')

            payload = jwt.decode(token[1], JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])

            # To check whether the token is expired or not
            if payload.get("expired_at") < int(datetime.utcnow().timestamp()):
                raise TokenExpired
            user = User.objects.get(pk=payload.get("user_id"), is_active=True)
            request.user = user
            if user.user_type in ['admin','partner'] :
                return True
            else:
                return False
        except User.DoesNotExist:
            raise UnauthorizedAccess
        except TokenExpired:
            raise TokenExpired
        except Exception:
            raise UnauthorizedAccess