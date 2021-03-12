from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CreatePostForm
from django.views.generic.list import ListView
from .models import Post,Comments,Like
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreatePostForm,UpdatePostForm
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

@login_required
def Update(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == "POST":
        form = UpdatePostForm(request.POST,instance=post)
        image = form.cleaned_data("image")
        post.image = image
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UpdatePostForm()
    return render(request,"posts/update.html",{"form":form})

"""class Publish(CreateView): # new
    model = Post
    form_class = CreatePostForm
    template_name = 'posts/publish.html'
    success_url = reverse_lazy('home')
"""
def home(request):
    """ display posts on the home page """
    posts = Post.objects.all()
    return render(request,"posts/home.html",{"posts":posts})

class PostDetail(DetailView):
    model = Post
    template_name = "posts/detail.html"
    context_object_name = "post"