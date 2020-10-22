"""View of Industry"""

from rest_framework.viewsets import ModelViewSet

from industry.models import Industry
from industry.serializers import IndustrySerializer


class IndustryViewSet(ModelViewSet):
    """View of Industry"""
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer
