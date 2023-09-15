from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method=='POST':
        
        user_name=request.POST['username']
        password=request.POST['password']
    
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Yoh have been logged in!!!")
            return redirect('home')  
        else:
            
            messages.success(request,"Error in login try again!")
            return redirect('home') 
    else:
        return render(request, 'home.html', {})

# def login_user(request):
#     pass 

def logout_user(request):
    logout(request) 
    messages.success(request,"You have been logged Out!!!")
    return redirect('home')