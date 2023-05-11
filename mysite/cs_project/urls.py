from django.urls import path
from django.contrib import admin, auth
from .views import index


urlpatterns = [
    path('', index, name='home'),
]