from django.urls import path, include
from categories.views import *

urlpatterns = [
    path('add/', add_category, name='add_category')
] 