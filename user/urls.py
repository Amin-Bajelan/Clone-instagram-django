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

]
