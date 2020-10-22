"""Serializer of Instrumentation"""

from rest_framework import serializers

from instrumentation.models import Instrumentation


class InstrumentationSerializer(serializers.ModelSerializer):
    """Serializer Class of Instrumentation"""
    instrumentation_type = serializers.ReadOnlyField()
    industry = serializers.ReadOnlyField()

    class Meta:
        """Meta Class"""
        model = Instrumentation
        fields = '__all__'
