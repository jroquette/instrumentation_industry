"""View of Industry"""

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from instrumentation.models import Instrumentation
from instrumentation.serializers import InstrumentationSerializer


class InstrumentationViewSet(ModelViewSet):
    """View of Industry"""
    queryset = Instrumentation.objects.all()
    serializer_class = InstrumentationSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request)
        except:
            response = {'message': 'All required fields have not been filled.'}
            return Response(response, status=status.HTTP_412_PRECONDITION_FAILED)

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request)
        except:
            response = {'message': 'All required fields have not been filled.'}
            return Response(response, status=status.HTTP_412_PRECONDITION_FAILED)
