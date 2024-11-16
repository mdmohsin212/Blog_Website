from django.urls import path, include
from author.views import *

urlpatterns = [
    path('add/', add_author, name='add_author'),
]
