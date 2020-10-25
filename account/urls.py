"""Urls of Account"""

from rest_framework import routers

from account.views import AccountViewSet


router = routers.DefaultRouter()
router.register(r'', AccountViewSet, basename='account')

account_urls = router.urls
