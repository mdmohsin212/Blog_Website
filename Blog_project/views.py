from django.shortcuts import render
from post.models import Post
from categories.models import Category

def home(request, category_slug=None):
    data = Post.objects.all()
    if category_slug is not None:
        try:
            category = Category.objects.get(slug=category_slug)
            data = Post.objects.filter(catagory=category)
        except Category.DoesNotExist:
            data = Post.objects.none()

    categories = Category.objects.all()
    return render(request, 'home.html', {'data': data, 'catagory': categories})
