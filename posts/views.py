from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import CreatePostForm
from django.views.generic.list import ListView
from .models import Post,Comments,Like
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
# Create your views here.


@login_required
def Publish(request):
    if request.method == "POST":
        form = CreatePostForm(request.POST,request.FILES)
        if form.is_valid():
            form.instance.publisher = request.user
            form.save()
            return redirect("home")
    else:
        form = CreatePostForm()

    return render(request,"posts/publish.html",{
        "form":form,
    })

"""class Publish(CreateView): # new
    model = Post
    form_class = CreatePostForm
    template_name = 'posts/publish.html'
    success_url = reverse_lazy('home')
"""
def home(request):
    return render(request,"posts/home.html")