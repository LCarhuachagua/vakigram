from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostsFeedView.as_view(), name='feed'),
    path('posts/new/', views.CreatePostView.as_view(), name='created_post'),
    path(
        route='posts/<int:pk>/',
        view= views.PostDetailView.as_view(),
        name='detail_post'
    )
]