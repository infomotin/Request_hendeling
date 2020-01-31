from django.db import models

# Create your models here.
class Menufacture(models.Model):
    manufacture = models.CharField(max_length= 20)
    destinations = models.CharField(max_length =30)
    any_discunts = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.manufacture

class Product(models.Model):
    menufacture = models.ForeignKey(Menufacture,on_delete=models.CASCADE,related_name="products")
    name = models.CharField(max_length=100)
    descriptions = models.TextField(blank=True,null=True)
    price = models.FloatField(max_length=100)
    photo = models.ImageField(blank=True,null=True,upload_to='img/')
    shipping_cost = models.FloatField()
    qty = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

