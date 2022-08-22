from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('', include('django.contrib.auth.urls')),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    path('create/', views.create, name='create'),
    path('my_posts/', views.my_posts, name='my_posts'),
]