from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path 
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from . import views
router = DefaultRouter()
router.register(r'Users', views.UsersView, basename='Users')
router.register(r'Complaints', views.ComplaintsView, basename='Complaints')
router.register(r'Organs', views.OrgansView, basename='Organs')
urlpatterns = router.urls
