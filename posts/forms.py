from django import forms
from .models import Post,Comments

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
        model = Comments
        fields = ['content',]