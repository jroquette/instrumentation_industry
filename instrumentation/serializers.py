"""Serializer of Client"""

from rest_framework import serializers

from instrumentation.models import Instrumentation


class InstrumentationSerializer(serializers.ModelSerializer):
    instrumentation_type = serializers.ReadOnlyField()
    industry = serializers.ReadOnlyField()

    class Meta:
        model = Instrumentation
        fields = '__all__'
