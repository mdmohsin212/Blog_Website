from django.urls import path, include
from author.views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('profile/pass_change/', pass_change, name='pass_change'),
    path('profile/edit/', edit_profile, name='edit_profile'),
]
