"""Urls of Instrumentation"""

from rest_framework import routers

from instrumentation.views import InstrumentationViewSet


router = routers.DefaultRouter()
router.register(r'', InstrumentationViewSet, basename='instrumentation')

instrumentation_urls = router.urls
