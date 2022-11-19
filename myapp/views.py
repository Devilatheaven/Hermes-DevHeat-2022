from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import student_details, teacher_details
from django.http import HttpResponse
# Create your views here.

global student_logged,teacher_logged
student_logged = 0
teacher_logged = 0

def index(request):
    global student_logged
    student_logged = 0
    return render(request,'index.html')
    
def home(request):
    global teacher_logged
    if teacher_logged == 1:
        return render(request,'home.html')
    else:
        return render(request,'tlogin.html')

def user(request):
    global student_logged
    if student_logged == 1:
        return render(request,'user.html')
    else:
        return render(request,'login.html')
    
def login(request):
    global student_logged
    student_logged = 0
    if request.method == 'POST':
        email= request.POST['username']
        password = request.POST['password']
        student = auth.authenticate(request, username=email, password=password)
        if student is not None :
            auth.login(request,user)
            student_logged = 1
            return redirect('user')
        else:
            messages.info(request,"Login Credentials are not matched")
            return redirect('login')
    else:
        return render(request,'login.html')


def logout(request):
    global student_logged
    student_logged = 0
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
            if User.objects.filter(email = email).exists():
                messages.info(request,'email id is already in use!')
                return redirect('register')
            else:
                student = User.objects.create_user(username=email, password= password)
                student_data = student_details.objects.create(username = username , passwordtodb = password, emailid = email, number = number)
                student_data.save()
                student.save()
                return redirect('login')
    else:
        messages.info(request,"passwords are not matched!")
        return render(request,'register.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def tregister(request):
    if request.method == "POST":
        tfirstname = request.POST['tfirstname']
        tlastname = request.POST['tlastname']
        temail = request.POST['email']
        tnumber = request.POST['phone']
        tpassword = request.POST['password']
        tpassword2 = request.POST['password2']
        print("finished input")
        if tpassword == tpassword2:
            if teacher_details.objects.filter(temail = temail).exists():
                print("same email found")
                messages.info(request,'email id is already in use!')
                return redirect('tregister')
            else:
                teacher = User.objects.create_user(username=temail, password= tpassword)
                teacher_data = teacher_details.objects.create(tfirstname = tfirstname ,tlastname = tlastname, tpassword = tpassword, temail = temail, tnumber = tnumber)
                teacher_data.save()
                teacher.save()
                print("saved")
                return redirect('tlogin')
        else:
            print("pass dont match")
            messages.info(request,'Passwords do not match!')
            return redirect('tregister')
    else:
        print("else //")
        return render(request,'tregister.html')

def tlogin(request):
    global teacher_logged
    teacher_logged = 0
    if request.method == 'POST':
        email= request.POST['username']
        password = request.POST['password']
        teacher = auth.authenticate(request, username=email, password=password)
        if teacher is not None :
            auth.login(request,user)
            teacher_logged = 1
            return redirect('home')
        else:
            messages.info(request,"Login Credentials are not matched")
            return redirect('tlogin')
    else:
        return render(request,'tlogin.html')        