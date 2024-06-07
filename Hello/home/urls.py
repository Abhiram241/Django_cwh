# This is my django

from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about,name="about"),
    path('contact/', views.contact,name="contact"),
    path('feedback/', views.feedback,name="feedback"),
    path('logoutuser/', views.logoutuser,),
]
