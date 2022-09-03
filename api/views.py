from rest_framework import serializers, generics
from books.models import Book
# Create your views here.

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle', 'author', 'isbn')

class BookAPI(generics.ListAPIView):
    queryset = Book.objects.filter()
    serializer_class = BookSerializers