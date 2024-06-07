from django.contrib import admin
from django.urls import path,include
from labs1 import views


urlpatterns = [
    path('', views.index),
]
