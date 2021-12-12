from django.shortcuts import redirect, render
from django.contrib import messages
from urllib import request
from .models import Post
from .models import Post_f_a
from django.contrib.auth.models import User,auth
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')

def loginform(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def regi_input(request):
    username=request.POST['username']
    email=request.POST['email']
    password=request.POST['password']
    password_confirm=request.POST['password_confirm']
    print(username)
    if password==password_confirm :
        if User.objects.filter(username=username).exists():
            messages.info(request,'UserName นี้มีคนใช้เเล้วครับ')
            return redirect('/register')
        elif User.objects.filter(email=email).exists():
            #print("Email นี้เคยลงทะเบียนเเล้ว")
            #return HttpResponse("Email นี้เคยลงทะเบียนเเล้ว") 
            messages.info(request,'Email นี้เคยลงทะเบียนเเล้ว')
            return redirect('/register')
        else :
            user=User.objects.create_user(
            username=username,
            password=password,
            email=email,
            )
            user.save()
            return render(request,'login.html')
    else :
        messages.info(request,'password มันผิดโว้ยยย!!!!')
        return redirect('/register')
        
#หน้า login เข้าสู่ระบบ        
def login(request):
        
    username=request.POST['username']
    password=request.POST['password']
    user=auth.authenticate(username=username, password=password)
    print(username)

    if user is not None :
        auth.login(request,user)
        print(username)
        #return render(request,'home.html')
        program = User.objects.all()
        return render(request, 'home.html', {'program': program})
        
    else :
        print(username)
        messages.info(request,'ไม่พบข้อมูล')
        return redirect('/loginform')
    
    #เเสดงข้อมูลหน้าเเรก
def home(request):
    program = User.objects.all()
    return render(request, 'home.html', {'program': program})
    
def profile(request):
    return render(request,'profile.html')
def test(request):
    program = User.objects.all()
    return render(request, 'test.html', {'program': program})
