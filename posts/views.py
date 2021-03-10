from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import CreatePostForm,CreatePostImageForm
from django.views.generic.list import ListView
from .models import Post,PostImage,Comments,Like
# Create your views here.


@login_required
def Publish(request):
    if request.method == "POST":
        captionForm = CreatePostForm(request.POST)
        imageForm = CreatePostImageForm(request.FILES)
        if captionForm.is_valid() and imageForm.is_valid():
            captionForm.save()
            imageForm.save()
            return redirect("home")
    else:
        captionForm = CreatePostForm()
        imageForm = CreatePostImageForm()
    return render(request,"posts/publish.html",{
        "captionForm":captionForm,
        "imageForm": imageForm,
    })

def home(request):
    return render(request,"posts/home.html")