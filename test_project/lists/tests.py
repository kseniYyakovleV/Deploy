from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.models import TestFileField

from lists.views import home_page
# Create your tests here

class HomePageTest(TestCase):
    """home page test"""
    
        
    def test_can_save_a_POST_request(self):
        response=self.client.post("/", data={"item_text":"A new list item"})
        self.assertIn("A new list item", response.content.decode())
        self.assertTemplateUsed(response, "home.html")
        tff = TestFileField()
        tff.file="SW_Repin_mart_2023.xlsx"
        tff.save()
        
    




