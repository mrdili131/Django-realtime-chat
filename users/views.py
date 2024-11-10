from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from .models import User

class RegisterView(View):
    def get(self,request):
        form = RegisterForm()
        return render(request,'register.html',{"form":form})
    def post(self,request):
        form = RegisterForm(request.POST)
        print(form.errors)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = User(username=username)
            user.set_password(password)
            user.save()
            login(request,user)
            return redirect("home")
        return render(request,'register.html',{"form":form})


class LoginView(View):
    def get(self,request):
        form = LoginForm()
        return render(request,'login.html',{'form':form })

    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
        return render(request,'login.html',{'form':form})

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('home')
