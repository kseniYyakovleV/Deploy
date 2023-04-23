from django.db import models

# Create your models here.

class TestModel(models.Model):
    test_text_field = models.TextField()




class TestFileField(models.Model):
    file = models.FileField(upload_to="Dir/")