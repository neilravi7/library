from django.db import models
from django.conf import settings
# Create your models here.

class Post(models.Model):
    
    DRAFTED = 'DRAFTED'
    PUBLISHED = 'PUBLISHED'

    STATUS = (
        (DRAFTED, 'Drafted'),
        (PUBLISHED, 'Published'),
    )
    
    image = models.CharField(null=True, blank=True, max_length=300)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='author_created_posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=10, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'posts'
    
    def __str__(self):
        return self.title