from django.db import models

class Spare_parts(models.Model):
    title = models.CharField(max_length=30)
    type = models.CharField(max_length=40, null = True)
    image = models.CharField(max_length=10)
    brand = models.CharField(max_length=30)
    #analogue = models.CharField(max_length=30, default="Нет/No")
    unit = models.CharField(max_length=30)
    count = models.IntegerField(default=0)
    min = models.IntegerField()
    #department = models.CharField(max_length=40, default="M&U (SW)")
    #article = models.CharField(max_length=100, default="Spare parts and Service")
    MABP = models.FloatField()
    currency = models.CharField(max_length=2)
    storage = models.TextField()

    def get_cost(self):
        return(str(self.MABP)+' '+self.currency)

    
    def get_full_info(self):
        return {"title": self.title, "type": self.type, "image": self.image, "brand": self.brand, "unit": self.unit, "count": self.count, "min": self.min, "MABP": self.MABP, "currency": self.currency, "storage": self.storage}

    def get_main_info(self):
        return {"title": self.title, "type": self.type, "brand": self.brand, "storage": self.storage}
    
    @staticmethod
    def get_all():
        objects = Spare_parts.objects.all()
        dictionary = {}
        for object in objects:
            dictionary[object.id] = object.get_main_info()
        return dictionary
# Create your models here.
