from django.contrib import admin
from django.urls import path, include
from Blog_project.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('category/<slug:category_slug>/', home, name='category_wise_post'),
    path('author/', include('author.urls')),
    path('post/', include('post.urls')),
    path('category/', include('categories.urls')),
]