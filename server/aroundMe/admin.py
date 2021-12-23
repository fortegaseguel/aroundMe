from django.contrib import admin
from .models import Post, Comment, Profile, Relationship

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'content', 'timestamp', 'latitud', 'longitud')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'timestamp', 'comment_text')


admin.site.register(Profile)
admin.site.register(Relationship)