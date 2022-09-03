from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)

    class Meta:
        db_table = 'book'


    def __str__(self):
        return self.title