from django.db import models

from client.models import Client


class Industry(models.Model):
    name = models.CharField(max_length=30)
    latitude = models.FloatField()
    longitude = models.FloatField()
    id_cli = models.ForeignKey(Client, null=True,
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def client(self):
        return self.id_cli
