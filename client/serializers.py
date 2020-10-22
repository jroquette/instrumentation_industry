"""Serializer of Client"""

from rest_framework import serializers
from client.models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name']
