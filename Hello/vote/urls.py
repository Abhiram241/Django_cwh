# This is my django

from django.contrib import admin
from django.urls import path,include
from vote import views

urlpatterns = [
    path('<int:num>', views.home),
    path('<str:name>', views.printName)
    
]
