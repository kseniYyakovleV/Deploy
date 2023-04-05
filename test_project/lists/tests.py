from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from lists.views import home_page
# Create your tests here

class HomePageTest(TestCase):
    """home page test"""
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEquals(found.func, home_page)

    def test_home_page_returns_correct_page(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode("utf8")
        self.assertTrue(html.startswith("<html>"))
        self.assertIn("<title>To-Do lists</title>", html)
        self.assertTrue(html.endswith("</html>"))



