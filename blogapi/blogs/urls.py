from django.urls import path
from .views import BlogPostList, BlogPostDetail

urlpatterns = [
    # List and create blog posts
    path('', BlogPostList.as_view(), name='blogpost-list'),

    # Retrieve, update, and delete individual blog posts by their ID
    path('<int:id>/', BlogPostDetail.as_view(), name='blogpost-detail'),
]
