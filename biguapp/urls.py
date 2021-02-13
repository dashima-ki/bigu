from django.contrib import admin
from django.urls import path
from .views import funcselect

urlpatterns = [
    path('test/',funcselect)
]
