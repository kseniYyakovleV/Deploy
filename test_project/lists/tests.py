from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page
# Create your tests here

class HomePageTest(TestCase):
    """home page test"""
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEquals(found.func, home_page)

    def test_home_page_returns_correct_page(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, "home.html")
        
        




