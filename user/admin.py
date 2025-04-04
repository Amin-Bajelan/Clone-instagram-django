from django.contrib import admin
from .models import UserProfile, Post, Comment, Follow, FollowRequest


# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password')
    list_filter = ('username', 'email', 'password')


class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'caption', 'date_posted')
    list_filter = ('user', 'date_posted')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'date_created')
    list_filter = ('user', 'post', 'date_created')


class FollowAdmin(admin.ModelAdmin):
    list_display = ('follower', 'following', 'date_followed')
    list_filter = ('follower', 'following', 'date_followed')


class FollowRequestAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'created_at', 'is_accepted')
    list_filter = ('sender', 'receiver', 'created_at', 'is_accepted')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Follow, FollowAdmin)
admin.site.register(FollowRequest, FollowRequestAdmin)
