"""Serializer Account"""

from rest_framework import serializers
from account.models import Account


class AccountSerializer(serializers.ModelSerializer):
    """Serializer Class of Account"""
    class Meta:
        """Meta Class"""
        model = Account
        exclude = ['password']
