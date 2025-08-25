from rest_framework.views import APIView
from common.utils import CommonUtils
from rest_framework.permissions import AllowAny

class HealthCheck(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        """
        @description: This API used to check if server is active or not
        @param request:
        @return: "SUCCESS"
        """
        return CommonUtils.dispatch_success(request, "SUCCESS")
