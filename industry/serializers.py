"""Serializer of Industry"""

from rest_framework import serializers

from industry.models import Industry
from client.serializers import ClientSerializer


class IndustrySerializer(serializers.ModelSerializer):
    """Serializer Class of Industry"""
    client = ClientSerializer(read_only=True)

    class Meta:
        """Meta Class"""
        model = Industry
        fields = ['name', 'longitude', 'latitude', 'id_cli', 'client']
        extra_kwargs = {'id_cli': {'write_only': True}}
