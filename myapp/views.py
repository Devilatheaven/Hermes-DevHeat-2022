from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import user_details
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'index.html')

def user(request):
    return render(request,'user.html')
    
def login(request):
    if request.method == 'POST':
        username= request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None :
            auth.login(request,user)
            return redirect('user')
        else:
            messages.info(request,"Login Credentials are not matched")
            return redirect('login')
    else:
        return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('home.html')

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        number = request.POST['number']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request,'User name is already in use!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password= password)
                user_data = user_details.objects.create(username = username , passwordtodb = password, emailid = email, number = number)
                user_data.save();
                user.save();
                return redirect('login')
    else:
        messages.info(request,"passwords are not matched!")
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def contactus(request):
    return redirect(request,'contactus.html')

def aboutus(request):
    return redirect(request,'aboutus.html')