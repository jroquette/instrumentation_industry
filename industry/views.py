"""View of Industry"""

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from industry.models import Industry
from industry.serializers import IndustrySerializer


class IndustryViewSet(ModelViewSet):
    """View of Industry"""
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request)
        except:
            response = {'message': 'All required fields have not been filled.'}
            return Response(response, status=status.HTTP_412_PRECONDITION_FAILED)

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request)
        except:
            response = {'message': 'All required fields have not been filled.'}
            return Response(response, status=status.HTTP_412_PRECONDITION_FAILED)