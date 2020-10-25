from rest_framework import authentication
from rest_framework import exceptions


class CustomAuthentication(authentication.BasicAuthentication):
    """Custom Authentication"""
    def authenticate(self, request):
        """Override of authenticate method"""
        try:
            response = super().authenticate(request)
            return response
        except:
            raise exceptions.PermissionDenied("Credentials Invalid.")
