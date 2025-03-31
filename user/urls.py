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

]
