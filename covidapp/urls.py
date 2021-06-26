
from .views import helloworldview
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('',helloworldview),
]
