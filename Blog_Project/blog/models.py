from django.db import models
from django.utils.text import slugify
from django.db import models
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.name






class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True)
    content = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    
    def __str__(self):
        return self.title
    