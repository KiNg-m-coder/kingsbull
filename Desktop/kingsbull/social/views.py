from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import Post, UserProfile, Comment, Like

def home(request):
    if request.user.is_authenticated:
        return redirect('second_page')
    return render(request, 'social/home.html')

def feed(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'social/feed.html', {'posts': posts})

def profile(request, username):
    user_profile = UserProfile.objects.get(user__username=username)
    posts = Post.objects.filter(user=user_profile.user).order_by('-created_at')
    return render(request, 'social/profile.html', {'user_profile': user_profile, 'posts': posts})

def add_comment(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        content = request.POST.get('content')
        Comment.objects.create(post=post, user=request.user, content=content)
    return redirect('feed')

def like_post(request, post_id):
    post = Post.objects.get(id=post_id)
    Like.objects.create(post=post, user=request.user)
    return redirect('feed')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('second_page')
        else:
            error_message = "Invalid username or password. Please try again."
            return render(request, 'social/login.html', {'error_message': error_message})
    return render(request, 'social/login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            auth_login(request, user)
            return redirect('second_page')
        except IntegrityError:
            error_message = "Username already exists. Please choose a different username."
            return render(request, 'social/signup.html', {'error_message': error_message})
    return render(request, 'social/signup.html')

def second_page(request):
    if not request.user.is_authenticated:
        return redirect('home')
    return render(request, 'social/second_page.html')

def logout_view(request):
    auth_logout(request)
    return render(request, 'social/logout.html')

def games_page(request):
    return render(request, 'games/games_page.html')

def social_page(request):
    return render(request, 'social/social_page.html')
