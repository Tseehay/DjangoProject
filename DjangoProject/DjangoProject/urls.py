"""
URL configuration for DjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]


# create a code 
from __future__ import unicode_literals

from django.urls import re_path

from .views import Rate
from . import app_settings


urlpatterns = [
    re_path(r'(?P<content_type_id>\d+)/(?P<object_id>' + app_settings.STAR_RATINGS_OBJECT_ID_PATTERN + ')/', Rate.as_view(), name='rate'),
]

app_name = 'star_ratings'