from rest_framework import serializers, generics
from books.models import Book
# Create your views here.

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle', 'author', 'isbn')

class BookAPIList(generics.ListAPIView):
    queryset = Book.objects.filter()
    serializer_class = BookSerializers

class BookAPIDetails(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers