from django.urls import path
from django.contrib import admin, auth
from .views import index
from . import views


urlpatterns = [
    path('', index, name='home'),
    path('register/', views.register, name='register'),
    path('add/', views.add_note, name='add')
]