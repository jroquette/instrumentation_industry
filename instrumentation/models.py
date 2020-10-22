"""Model File of Instrumentation"""

from django.db import models

from industry.models import Industry


class Instrumentation(models.Model):
    """Model of Instrumentation"""
    name = models.CharField(max_length=30)
    instrumentation = models.PositiveIntegerField(default=0)
    equation = models.FloatField()
    installation_quota = models.FloatField()
    attention_value = models.FloatField()
    id_ind = models.ForeignKey(Industry, null=True,
                               on_delete=models.CASCADE)

    def __str__(self):
        """Magic Method of Instrumentation"""
        return self.name

    def instrumentation_type(self):
        """Get Instrumentation type"""
        if self.instrumentation == 0:
            return 'Valve'
        return 'Piezometer'
