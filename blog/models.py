from django.conf import settings
from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=63, unique=True)
    slug = models.SlugField(max_length=63, unique=True)
    content = models.TextField(max_length=255, blank=True)
    category_image = models.ImageField(upload_to='photos/categories/', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('posts_by_category', args=[self.slug])

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=511)
    slug = models.SlugField(max_length=511, unique=True)
    content = models.TextField(blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    published = models.BooleanField(default=True)
    pin_top = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField()
    category = models.ManyToManyField(Category, related_name='posts')
    post_image = models.ImageField(upload_to='photos/posts', blank=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=127, null=True, blank=True)
    email = models.CharField(max_length=255)
    comment = models.TextField(blank=True)
    actived = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)