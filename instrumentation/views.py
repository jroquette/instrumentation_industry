"""View of Industry"""

from rest_framework.viewsets import ModelViewSet

from instrumentation.models import Instrumentation
from instrumentation.serializers import InstrumentationSerializer


class InstrumentationViewSet(ModelViewSet):
    """View of Industry"""
    queryset = Instrumentation.objects.all()
    serializer_class = InstrumentationSerializer
