from . import views
from django.urls import path



urlpatterns = [
    path('signup/', views.registration, name='registration'),
    path('login/',views.login,name='login'),
    path('',views.index,name='index')
]
