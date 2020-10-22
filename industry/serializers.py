"""Serializer of Industry"""

from rest_framework import serializers

from industry.models import Industry
from client.serializers import ClientSerializer


class IndustrySerializer(serializers.ModelSerializer):
    """Serializer Class of Industry"""
    client = ClientSerializer()

    class Meta:
        """Meta Class"""
        model = Industry
        exclude = ['id_cli']
