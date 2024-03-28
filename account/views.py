from django.shortcuts import render, redirect
from django import views
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from account.models import CustomUser

class RegisterView(views.View):
    def get(self, request):
        return render(request, "account/register.html")
    
    def post(self, request):
        data = request.POST
        user = CustomUser.objects.create(
            name = data["name"],
            email = data["email"],
            phone = data["phone"],
        )
        user.set_password(data["password"])
        user.save()
        return redirect("account:login")

class LoginView(views.View):
    def get(self, request):
        return render(request, "account/login.html")
    
    def post(self, request):
        print(request.POST)
        email = request.POST["email"]
        password = request.POST["password"]
        print(email)
        print(password)
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
        else:
            messages.error(request,"Invalid Credentials")
            return redirect("account:login")

        return redirect("/")

def logout_view(request):
    logout(request)
    return redirect("account:login")