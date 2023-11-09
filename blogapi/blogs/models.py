from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=200, blank=True)
    featured_image = models.URLField(null=True, blank=True)
    # featured_image = models.ImageField(upload_to='blog_images/', null=True, blank=True)

    # Add a field for a short description or excerpt of the blog post
    excerpt = models.TextField(blank=True)

    # Add a field for the number of views or reads of the blog post
    views = models.PositiveIntegerField(default=0)

    # Add a field for the number of likes or upvotes
    likes = models.PositiveIntegerField(default=0)
