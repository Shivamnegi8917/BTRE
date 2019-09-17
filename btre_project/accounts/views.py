from django.shortcuts import render,redirect
from django.contrib import messages,auth

# Create your views here.
def register(request):
    if request.method=='POST':
        messages.error(request,'Testing error message') 
        return redirect('register') 

    else:
        return render(request,'accounts/register.htm')

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"You are now logged in")
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid credentials')
            return redirect('login') 
    else:
        return render(request,'accounts/login.htm')

def logout(request):
    if request.method=='POST':
        auth.logout(request)
        messages.success(request,"You are now logged out")  
        return redirect('index')
def dashboard(request):
    return render(request,'accounts/dashboard.htm')

