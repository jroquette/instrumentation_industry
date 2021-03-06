"""instrumentation_industry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from client.urls import client_urls
from industry.urls import industry_urls
from instrumentation.urls import instrumentation_urls
from account.urls import account_urls


urlpatterns = [
    path('client/', include(client_urls)),
    path('account/', include(account_urls)),
    path('industry/', include(industry_urls)),
    path('instrumentation/', include(instrumentation_urls)),
    path('admin/', admin.site.urls),
    path('get_token/', obtain_auth_token, name='login'),
]
