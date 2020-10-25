"""View of Client"""

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from client.models import Client
from client.serializers import ClientSerializer


class ClientViewSet(ModelViewSet):
    """View of Client"""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

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
