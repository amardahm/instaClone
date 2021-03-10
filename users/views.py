from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import UserRegisterForm
from django.contrib import messages
# Create your views here.
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def registerUserView(request):
    """ this is for registring a new user"""
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'your account has been created successfully! you are able to login')
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request,"users/register.html",{"form":form})