from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book, Author
from django.contrib.auth.models import User


class BookAPITestCase(TestCase):
    def setUp(self):
        # Create a user and obtain a token
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client = APIClient()
        self.client.login(username='testuser', password='password123')

        # Create sample authors and books
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book = Book.objects.create(title="Harry Potter", author=self.author, publication_year=2000)

        # API endpoints
        self.list_url = '/books/'
        self.detail_url = f'/books/{self.book.id}/'
        self.create_url = '/books/create/'
        self.update_url = f'/books/{self.book.id}/update/'
        self.delete_url = f'/books/{self.book.id}/delete/'

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Harry Potter")

    def test_create_book(self):
        data = {
            "title": "Fantastic Beasts",
            "author": self.author.id,
            "publication_year": 2016
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book(self):
        data = {"title": "Harry Potter Updated"}
        response = self.client.put(self.update_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Harry Potter Updated")

    def test_delete_book(self):
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books_by_author(self):
        response = self.client.get(self.list_url + f"?author__name={self.author.name}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_authentication_required(self):
        # Test without authentication
        self.client.logout()
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_filter_books_by_publication_year(self):
        response = self.client.get(self.list_url + "?publication_year=2000")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        response = self.client.get(self.list_url + "?search=Harry")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books_by_title(self):
        response = self.client.get(self.list_url + "?ordering=title")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], "Fantastic Beasts")




