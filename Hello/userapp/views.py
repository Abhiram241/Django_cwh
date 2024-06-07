from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

from django.contrib.auth import logout
# Create your views here.

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request=request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/ua")
        else:
            return render(request, "ulogin.html")
    return render(request, 'ulogin.html')

def logoutuser(request):
    logout(request)
    return redirect("/ua/login")

def home(request):
    if request.user.is_anonymous:
        return redirect("/ua/login/")

    return render(request, "uhome.html")