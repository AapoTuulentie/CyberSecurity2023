from django.urls import path
from django.contrib import admin, auth
from . import views


urlpatterns = [
    path('', views.viewnotes, name='home'),
    path('register/', views.register, name='register'),
    path('add/', views.add_note, name='add'),
    path('delete/<int:noteid>', views.deletenote, name='delete'),
]