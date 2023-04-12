import unittest
from flask import Flask
from flask_testing import TestCase
from app import app, posts, comments, users

class AppTestCase(TestCase):
    def create_app(self):
        return app

    def test_index_route(self):
        response = self.client.get('/')
        self.assert200(response)
        self.assertTemplateUsed('index.html')

    def test_posty_route_with_valid_search_term(self):
        search_term = "sunt"
        response = self.client.post('/posty', data={'searchbox': search_term})
        self.assert200(response)
        self.assertTemplateUsed('posty.html')
        self.assertIn(search_term, str(response.data))
    
    def test_posty_route_with_invalid_search_term(self):
        search_term = "invalid_search_term"
        response = self.client.post('/posty', data={'searchbox': search_term})
        self.assert200(response)
        self.assertTemplateUsed('posty.html')
        self.assertNotIn(search_term, str(response.data))

    def test_posts_data_loaded(self):
        self.assertIsNotNone(posts)
        self.assertIsInstance(posts, list)
        self.assertGreater(len(posts), 0)

    def test_comments_data_loaded(self):
        self.assertIsNotNone(comments)
        self.assertIsInstance(comments, list)
        self.assertGreater(len(comments), 0)

    def test_users_data_loaded(self):
        self.assertIsNotNone(users)
        self.assertIsInstance(users, list)
        self.assertGreater(len(users), 0)

if __name__ == '__main__':
    unittest.main(exit=False)
