from django.shortcuts import render,redirect
from .form import UserModelForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib import messages
# from Project.urls import *
from .models import Profile



# Create your views here.

def userLogin(request):
    
    form = UserModelForm()
    context = {'form':form}
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except: 
            messages.error(request, 'Username does not exist!') 

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            print("User successfully logged in!")
            return redirect('home')
        else:
            messages.error(request, 'username or password is not valid!!!')
    return render(request, 'User/login.html', context)


def userLogout(request):
    logout(request)
    print("User successfully logged out!")
    return redirect('login')


def userProfile(request):
    profile = Profile.objects.all()
    return render(request, 'User/profile.html', {'profile':profile})
