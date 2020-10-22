"""Model File of Industry"""

from django.db import models

from client.models import Client


class Industry(models.Model):
    """Model of Industry"""
    name = models.CharField(max_length=30)
    latitude = models.FloatField()
    longitude = models.FloatField()
    id_cli = models.ForeignKey(Client, null=True,
                               on_delete=models.CASCADE)

    def __str__(self):
        """Magic class of Industry"""
        return self.name

    def client(self):
        """Client data"""
        return self.id_cli
