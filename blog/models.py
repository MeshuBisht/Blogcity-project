from django.db import models

# Create your models here.
from django.contrib.auth.models import User


CATEGORY_CHOICES = (
    
    ('technology', 'Technology'),
    ('sports','Sports'),
    ('nature','Nature'),
    ('world','world'),
    ('travel','Travel'),

)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField(max_length=2000000)
    created_on = models.DateTimeField(auto_now_add=True)
    #status = models.IntegerField(choices=STATUS, default=0)
    category = models.CharField(max_length=12, choices=CATEGORY_CHOICES,)
    imgfile= models.ImageField(upload_to='images/', default='', null=True, blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title