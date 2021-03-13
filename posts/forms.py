from django import forms
from .models import Post,Comment

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['caption','image']

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['caption','image']
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content',]