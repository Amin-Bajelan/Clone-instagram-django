from django.urls import path
from . import views

urlpatterns = [
    path('', views.first_page, name='first_page'),
    path('index/', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('add_post/', views.add_post, name='add_post'),
    path('show_user_profiles/<int:user_id>', views.show_user_profiles, name='show_user_profiles'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('comment_post/<int:post_id>',views.comment_post, name='comment_post'),
    path('show_comments/<int:post_id>', views.show_comments, name='show_comments'),
    path('create_follow_user/<int:message_id>', views.create_follow_user, name='create_follow_user'),
    path('delete_follow_user/<int:message_id>', views.delete_follow_user, name='delete_follow_user'),
    path('show_follow_request', views.show_follow_request, name='show_follow_request'),
    path('follow_user_request/<int:user_id>', views.follow_user_request, name='follow_user_request'),

    path('show_follow/<int:user_id>', views.show_follow, name='show_follow'),

]
