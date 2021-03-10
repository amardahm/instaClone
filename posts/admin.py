from django.contrib import admin
from .models import Post,PostImage,Comments,Like
# Register your models here.

admin.site.register(Post)
admin.site.register(PostImage)
admin.site.register(Comments)
admin.site.register(Like)
