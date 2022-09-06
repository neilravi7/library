from rest_framework import serializers
from . import models

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = ['id', 'author', 'title', 'body']
