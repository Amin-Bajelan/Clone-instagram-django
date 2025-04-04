from datetime import timezone

from django.db import models
from datetime import datetime


# Create your models here.

class UserProfile(models.Model):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=8)
    bio = models.TextField(max_length=150, blank=True)
    profile_picture = models.ImageField(upload_to='photos/', null=True, blank=True,
                                        default='https://www.google.com/url?sa=i&url=https%3A%2F%2Fcommons.wikimedia.org%2Fwiki%2FFile%3ADefault_pfp.jpg&psig=AOvVaw3fhkfUk6VXN-Uc9y-dKrIW&ust=1743369946894000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCKDLpKSdsIwDFQAAAAAdAAAAABAE')
    date_joined = models.DateTimeField(auto_now_add=True)
    followers = models.PositiveIntegerField(default=0)
    following = models.PositiveIntegerField(default=0)
    post_count = models.PositiveIntegerField(default=0)
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username} {self.email} {self.password}"


class Post(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/', blank=False, null=False)
    likes = models.PositiveIntegerField(default=0)
    liked_by = models.ManyToManyField(UserProfile, blank=True, related_name='liked_posts')
    caption = models.TextField(max_length=200, blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} {self.likes} "


class Comment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(max_length=300)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.date_created}"


class Follow(models.Model):
    follower = models.ForeignKey(UserProfile, related_name="following_related", on_delete=models.CASCADE)
    following = models.ForeignKey(UserProfile, related_name='follower_related', on_delete=models.CASCADE)
    date_followed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"follow from :{self.follower} to {self.following} at {self.date_followed}"


class FollowRequest(models.Model):
    sender = models.ForeignKey(UserProfile, related_name='sent_requests', on_delete=models.CASCADE)
    receiver = models.ForeignKey(UserProfile, related_name='received_requests', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.sender} {self.receiver} {self.is_accepted}"
