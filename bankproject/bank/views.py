from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.shortcuts import render, redirect

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        password1=request.POST['cpassword']
        if password==password1:

            if User.objects.filter(username=username).exists():
                messages.info(request, "username Taken")
                return redirect('bank:register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
                messages.info(request, "User Registered")
                return redirect('bank:login')
        else:
            messages.info(request,"password not matching")
            return redirect('bank:register')
        return redirect('bank:login')
    return render(request,"register.html")
# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('bank:x')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('bank:login')
    return render(request,'login.html')


def index(request):
    return render(request,"index.html")
def x(request):
    return render(request,"x.html")
def f(request):
    return render(request,"f.html")
def form(request):
    if request.method == 'POST':
        messages.info(request, "Application Accepted")
    return render(request,"form.html")