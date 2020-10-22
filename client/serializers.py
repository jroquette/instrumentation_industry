"""Serializer of Client"""

from rest_framework import serializers
from client.models import Client


class ClientSerializer(serializers.ModelSerializer):
    """Serializer Class of Client"""
    class Meta:
        """Meta Class"""
        model = Client
        fields = ['id', 'name']
