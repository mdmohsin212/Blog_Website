from django.shortcuts import render, redirect
from post.forms import PostFrom
from post.models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def add_post(request):
    if request.method == 'POST':
        post_form = PostFrom(request.POST)
        if post_form.is_valid():
            # post_form.cleaned_data['author'] = request.user
            post_form.instance.author = request.user
            post_form.save()
            return redirect('home')
    else:
        post_form = PostFrom()
    return render(request, 'add_post.html', {'form' : post_form})


@login_required
def edit_post(request, id):
    post = Post.objects.get(pk=id)
    post_form = PostFrom(instance=post)
    if request.method == 'POST':
        post_form = PostFrom(request.POST, instance=post)
        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.save()
            return redirect('home')
        
    return render(request, 'add_post.html', {'form' : post_form})

@login_required
def delete_post(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('home')