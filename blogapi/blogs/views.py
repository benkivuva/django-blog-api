from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from .models import BlogPost
from .serializers import BlogPostSerializer

class BlogPostList(ListCreateAPIView):
    serializer_class = BlogPostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        # Return all blog posts, not just those of the current user
        return BlogPost.objects.all()

class BlogPostDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = BlogPostSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        # Return all blog posts, not just those of the current user
        return BlogPost.objects.all()
