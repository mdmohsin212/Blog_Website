from django.shortcuts import render, redirect
from author.forms import *
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from post.models import *

# Create your views here.
def register(request):
    if request.method == 'POST':
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Accout Created Successfully')
            return redirect('login')
    else:
        register_form = RegistrationForm()
    return render(request, 'register.html', {'form' : register_form, 'type' : 'Register'})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username = user_name,password = user_pass)
            if user is not None:
                messages.success(request, 'Login Successfully')
                login(request, user)
                return redirect('profile')
            else:
                messages.warning(request, 'Login informantion incorrect')
                return redirect('login')
    else:
        form = AuthenticationForm()
    return render(request, 'register.html', {'form' : form, 'type' : 'login'})

def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = ChangeUserForm(request.POST, instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile')
    else:
        profile_form = ChangeUserForm(instance=request.user)
    return render(request, 'update_profile.html', {'form' : profile_form})

@login_required
def profile(request):
    data = Post.objects.filter(author = request.user)
    return render(request, 'profile.html', {'data' : data})

@login_required
def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Updated Successfully')
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'pass_change.html', {'form' : form})


# 123456SI
# 123456SM