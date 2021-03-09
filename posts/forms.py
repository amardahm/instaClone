from django import forms
from .models import Post,Comments,PostImage

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['caption']

class CreatePostImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ['image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['content',]