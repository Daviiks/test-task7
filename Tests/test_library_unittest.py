import unittest
from src.library import Library


class TestLibrary(unittest.TestCase):
    def setUp(self):
        """Выполняется перед каждым тестом"""
        self.library = Library()
        self.sample_books = [
            {"title": "Book 1", "author": "Author A"},
            {"title": "Book 2", "author": "Author B"},
            {"title": "Book 3", "author": "Author A"},
        ]
        
    def test_add_book(self):
        """Тест добавления книги"""
        self.library.add_book("New Book", "New Author")
        self.assertIn({"title": "New Book", "author": "New Author"}, self.library.books)
        print(self.library.books)
    
    def test_remove_book(self):
        """Тест удаления книги"""
        for book in self.sample_books:
            self.library.add_book(book["title"], book["author"])
        
        self.library.remove_book("Book 1")
        self.assertEqual(len(self.library.books), 2)
        print(self.library.books)
    
    def test_find_books_by_author(self):
        """Тест поиска книг по автору"""
        for book in self.sample_books:
            self.library.add_book(book["title"], book["author"])
        
        found_books = self.library.find_books_by_author("Author A")
        self.assertCountEqual(found_books, ["Book 1", "Book 3"])  # Проверка без учета порядка

