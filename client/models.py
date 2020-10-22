"""Model File of Client"""

from django.db import models


class Client(models.Model):
    """Model of Client"""
    name = models.CharField(max_length=30)

    def __str__(self):
        """Magic method client"""
        return self.name
