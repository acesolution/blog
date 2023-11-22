from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('regular', 'Regular User'),
        ('blogger', 'Blogger'),
        ('superuser', 'Superuser'),
    )

    user_type = models.CharField(
        max_length=10,
        choices=USER_TYPES,
        default='regular',
    )

    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    


class BlogPost(models.Model):
    title = models.CharField(max_length=500)
    read_time = models.IntegerField()
    post_image = models.ImageField(upload_to='blog_image/')
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    content = models.TextField()  # This field will store the HTML content
    created_date = models.DateField(auto_now=True)
   

    def __str__(self):
        return self.title
    