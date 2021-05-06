from django.shortcuts import render,redirect
# from .forms import CustomUserCreationForm, registerForm
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from  django.contrib.auth.hashers import make_password

from django.shortcuts import HttpResponse, render, redirect
from django.conf import settings 
from .models import customUser
from django.http import JsonResponse
from django.contrib.auth import logout

from .forms import registerForm,UpdateForm
# Create your views here.


@login_required
def index(request):
    # if request.user:
    
    instance=customUser.objects.filter(id=request.user.id).first()
    form=UpdateForm(instance=instance)
    
    edit=False
    if request.method=="POST":
        form=UpdateForm(request.POST, request.FILES,instance=instance)
        edit=True
        if form.is_valid():
            user=form.save()
            edit=False
            form=UpdateForm(instance=instance)

    return render(request,"index.html",{"instance":instance,"form":form,"edit":edit})


def loginView(request):
    userd=customUser.objects.filter(is_superuser=True)
    if request.method=="POST":
        email=request.POST.get('Email')
        password=request.POST.get('password')
        print(email,password)
        user = authenticate(username=email ,password=password)
        print(user)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('home')
            else:
                msg="Your account is inactive."
                return render(request,"login.html",{'msg':msg})
        else:
             msg="Invalid login details given"
             return render(request,"login.html",{'msg':msg})

    return render(request,"login.html")


def register(request):
    form=registerForm()
    if request.method=='POST':
        form=registerForm(request.POST, request.FILES)
        print(request.FILES)
        print(form)
        if form.is_valid():
           
            password=form.cleaned_data.get('password')
            if password:
                user=form.save()
                user.password=make_password(user.password)

                user.save()
                login(request,user,backend='django.contrib.auth.backends.ModelBackend')
                print(user.password)
                return redirect('home')
        # print(form)
    return render(request,"register.html",{'form':form})


def logoutView(request):
        logout(request)
        return redirect('loginpage')