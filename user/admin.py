from django.contrib import admin
from .models import UserProfile,Post


# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password')
    list_filter = ('username', 'email', 'password')

class PostAdmin(admin.ModelAdmin):
    list_display = ('user','caption','date_posted')
    list_filter = ('user','date_posted')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Post, PostAdmin)
