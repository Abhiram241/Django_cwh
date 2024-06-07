from django.contrib import admin
from django.urls import path,include
from userapp import views

admin.site.site_header = "Techy Studio Admin"
admin.site.site_title = "Techy Studio Admin Portal"
admin.site.index_title = "Welcome to Techy Studio Portal"

urlpatterns = [
    path('login/',views.user_login),
    path('', views.home),
    path('logout/',views.logoutuser),


]




