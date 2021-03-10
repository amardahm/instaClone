from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import CreatePostForm,CreatePostImageForm
# Create your views here.


@login_required
def Publish(request):
    if request.method == "POST":
        captionForm = CreatePostForm(request.POST)
        imageForm = CreatePostImageForm(request.FILES)
        if captionForm.is_valid() and imageForm.is_valid():
            captionForm.save()
            imageForm.save()
            return redirect()
    else:
        captionForm = CreatePostForm()
        imageForm = CreatePostImageForm()
    return render(request,"posts/publish.html",{
        "captionForm":captionForm,
        "imageForm": imageForm,
    })

