from django.urls import path, include
from profiles.views import *

urlpatterns = [
    path('add/', add_profile, name='add_profile')
]