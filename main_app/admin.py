from django.contrib import admin
from .models import Post
from .models import Comment

admin.site.register(Post)
admin.site.register(Comment)