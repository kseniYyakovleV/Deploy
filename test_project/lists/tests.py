from django.test import TestCase
from django.urls import resolve
from lists.views import home_page

# Create your tests here

class HomePageTest(TestCase):
    """home page test"""
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEquals(found.func, home_page)
