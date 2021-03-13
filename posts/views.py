from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Post,Comments,Like
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreatePostForm,UpdatePostForm,CommentForm
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
def UpdatePost(request,pk):
    """vanilla view to update a post"""
    post = get_object_or_404(Post,pk=pk)
    if request.method == "POST":
        form = UpdatePostForm(request.POST,request.FILES,instance=post)
        if request.user == post.publisher:
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            return HttpResponse("<h1> you are not allowed to make this setting </h1>")
    else:
        form = UpdatePostForm()
    return render(request,"posts/update.html",{"form":form})

def DeletePost(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == "POST":
        if request.user == post.publisher:
            post.delete()
            return redirect("home")
        else:
            return HttpResponse("<h1> you are not allowed to go to this page</h1>")
    return render(request,"posts/delete.html")

@login_required
def CreateComment(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST or None)
        if form.is_valid():
            content = request.POST.get('content')
            comment = Comments(post=post,content=content,author=request.user)
            comment.save()
            return redirect('home')
    else:
        form = CommentForm()
    return render(request,"posts/comment.html",{"form":form})



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
    """class based view to display post details"""
    model = Post
    template_name = "posts/detail.html"
    context_object_name = "post"





