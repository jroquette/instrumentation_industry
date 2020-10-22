"""View of Client"""

from rest_framework.viewsets import ModelViewSet

from client.models import Client
from client.serializers import ClientSerializer


class ClientViewSet(ModelViewSet):
    """View of Client"""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
