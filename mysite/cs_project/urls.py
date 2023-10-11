from django.urls import path
from django.contrib import admin, auth
from .views import viewnotes, deletenote, searchnotes
from . import views


urlpatterns = [
    path('', viewnotes, name='home'),
    path('register/', views.register, name='register'),
    path('add/', views.add_note, name='add'),
    path('delete/<int:noteid>', deletenote, name='delete'),
    path('search/', searchnotes, name='search'),
]