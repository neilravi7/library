from django.conf import settings
from django.db import models

# Create your models here.
class Profile(models.Model):
    
    MALE = 'MALE'
    FEMALE = 'FEMALE'

    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_profile')
    age = models.PositiveIntegerField(default=0)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    address = models.CharField(null=True, blank=True, max_length=200)
    profile_image = models.CharField(null=True, blank=True, max_length=100)

    class Meta:
        db_table = 'profile'
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}' 