from rest_framework import routers

from client.views import ClientViewSet


router = routers.DefaultRouter()
router.register(r'', ClientViewSet, basename='client')

client_urls = router.urls