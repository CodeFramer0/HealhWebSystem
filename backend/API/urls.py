from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path 
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from . import views
router = DefaultRouter()
urlpatterns = router.urls
