"""Model File of Instrumentation"""

from django.db import models

from industry.models import Industry


class Instrumentation(models.Model):
    """Model of Instrumentation"""
    INSTRUMENTATION_TYPE = (
        (0, "Valve"),
        (1, "Piezometer")
    )
    instrumentation_type = models.PositiveIntegerField(choices=INSTRUMENTATION_TYPE,
                                                  null=False, blank=False)
    name = models.CharField(max_length=30)
    equation = models.FloatField()
    installation_quota = models.FloatField()
    attention_value = models.FloatField()
    id_ind = models.ForeignKey(Industry, null=True, related_name='instrumentation',
                               on_delete=models.CASCADE)

    def __str__(self):
        """Magic Method of Instrumentation"""
        return self.name
