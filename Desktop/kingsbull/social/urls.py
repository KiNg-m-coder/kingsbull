from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('feed/', views.feed, name='feed'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('add_comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('like_post/<int:post_id>/', views.like_post, name='like_post'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('second_page/', views.second_page, name='second_page'),
    path('logout/', views.logout_view, name='logout'),
    path('games/', views.games_page, name='games_page'),
    path('social_page/', views.social_page, name='social_page'),
]
