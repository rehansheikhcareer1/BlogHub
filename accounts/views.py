from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm, ProfileEditForm

def signup_view(request):
    """
    User registration
    """
    if request.user.is_authenticated:
        return redirect('blog:home')
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('blog:home')
    else:
        form = SignUpForm()
    
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    """
    User login
    """
    if request.user.is_authenticated:
        return redirect('blog:home')
    
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('blog:home')
    else:
        form = LoginForm()
    
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    """
    User logout
    """
    logout(request)
    messages.info(request, 'Logged out successfully.')
    return redirect('blog:home')

@login_required
def profile_view(request):
    """
    User profile page - shows user stats and recent activity
    """
    return render(request, 'accounts/profile.html')

@login_required
def profile_edit(request):
    """
    Edit user profile - update profile picture, bio, location, website
    """
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Profile updated successfully!')
            return redirect('accounts:profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ProfileEditForm(instance=request.user.profile)
    
    return render(request, 'accounts/profile_edit.html', {'form': form})
