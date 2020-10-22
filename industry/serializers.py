"""Serializer of Industry"""

from rest_framework import serializers

from industry.models import Industry
from client.serializers import ClientSerializer


class IndustrySerializer(serializers.ModelSerializer):
    client = ClientSerializer()

    class Meta:
        model = Industry
        exclude = ['id_cli']
