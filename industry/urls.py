from rest_framework import routers

from industry.views import IndustryViewSet


router = routers.DefaultRouter()
router.register(r'', IndustryViewSet, basename='industry')

industry_urls = router.urls
