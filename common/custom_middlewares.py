import re
from datetime import datetime

import jwt
from django.conf import settings
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from rest_framework import status
from rest_framework.permissions import AllowAny
from unicodedata import category

from common.permissions import TokenExpired, UnauthorizedAccess
from user.models import Blocklist


# from user.models import Blocklist, User


class AllowWhitelistedHostMiddleware:
    def __init__(self, view):
        self.view = view
        self.open_endpoints = [
            r'^/$',
            r'^/media/',
            r'^/admin/',
            r'^/api/calendar/',
            r'^/api/calendar/meeting/',
            r'^/api/agent/',
            r'^/api/chat/',
            r'^/api/user/',
            r'^/api/agent/category/',
            r'^/api/agent/category-list/',
            r'^/api/agent/accept-request/',
            r'^/api/docusign/',
            r'^/api/contact-tracing/',
            r'^/api/reports/',
            r'^/api/docusign/candidate/',
            r'^/api/notifications/',
        ]

    def __call__(self, request):
        url_path = request.get_full_path()
        for endpoint in self.open_endpoints:
            is_open = bool(re.match(endpoint, url_path))
            if is_open:
                break
        else:
            if not request.headers.get('Origin') or request.headers['Origin'] not in settings.CORS_ALLOWED_ORIGINS:
                return JsonResponse(
                    {"status": "failed", "code": 5000, "message": "Access Denied"},
                    status=status.HTTP_403_FORBIDDEN
                )
            return self.view(request)

        # Redirects the request to view and returns the response
        return self.view(request)


class JWTAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        public_paths = [
            r'^/',
            r'^/login/',
            r'^/signup/',
            r'^/admin/',
            r'^/media/',
        ]

        # Skip middleware for public endpoints
        request.csrf_processing_done = True
        if any(re.match(pattern, request.path) for pattern in public_paths):
            return

        if request.resolver_match is not None:
            view = request.resolver_match.func.view_class
            if hasattr(view, 'permission_classes') and AllowAny in view.permission_classes:
                return

        auth_header = request.META.get('HTTP_AUTHORIZATION', None)
        if auth_header is None:
            if "category" in request.path or request.path_info:
                return
            return JsonResponse({"error": "Authorization header missing"}, status=401)

        try:
            token_type, token = auth_header.split()
            if token_type.lower() != 'bearer':
                return JsonResponse({"error": "Invalid token type"}, status=401)

            # Check if token is in the blocklist
            if Blocklist.objects.filter(token=token).exists():
                return JsonResponse({"error": "Token has been invalidated (logged out)"}, status=401)

            # Decode and validate the token
            payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])

            # Check for token expiration
            if payload.get("expired_at") < int(datetime.utcnow().timestamp()):
                raise TokenExpired

            # Attach user to request
            user_id = payload.get("user_id")
            # try:
            #     request.user = User.objects.get(pk=user_id, is_active=True)
            # except User.DoesNotExist:
            #     raise UnauthorizedAccess

        except jwt.ExpiredSignatureError:
            return JsonResponse({"error": "Token has expired"}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({"error": "Invalid token"}, status=401)
        except UnauthorizedAccess:
            return JsonResponse({"error": "Unauthorized access"}, status=401)
        except TokenExpired:
            return JsonResponse({"error": "Token expired"}, status=401)
        except Exception as e:
            return JsonResponse({"error": "Authentication failed"}, status=401)