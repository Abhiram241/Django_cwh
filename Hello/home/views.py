from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def index(request):
    # return HttpResponse("<h1>This is index page</h1>")
    context1={
        'webuser':"Abhiram"
    }
    if request.user.is_anonymous:
        return redirect("/feedback/")
    return render(request,'index.html',context1)
def about(request):
    context={
        'Name':'Abhiram'
    }
    return render(request,'about.html',context)
    
def contact(request):
    context={
        'Name':'Abhiram'
    }
    if request.method == "POST":
        name = request.POST.get('name')
        mail = request.POST.get('mail')
        phone = request.POST.get('phone')
        contacting = request.POST.get('contacting')
        contact = Contact(name=name,mail=mail,phone=phone,contacting=contacting,date=datetime.today())
        contact.save()
        messages.success(request, "Thank you for your time!")

    return render(request,'contact.html',context)
    
def feedback(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request=request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, "feedback.html")
    return render(request, 'feedback.html')

def logoutuser(request):
    logout(request)
    return redirect("/")