from django.test import TestCase
from .models import Book

# Create your tests here.

class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title = "Greedy Dog",
            subtitle = "Greedy dog cross the river",
            author = "Panchtantra",
            isbn = "412375990667"
        )
    
    def test_book_content(self):
        self.assertEqual(self.book.title, "A good title")
        self.assertEqual(self.book.subtitle, "An excellent subtitle")
        self.assertEqual(self.book.author, "Tom Christie")
        self.assertEqual(self.book.isbn, "1234567890123")