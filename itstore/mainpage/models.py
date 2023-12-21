from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    description = models.CharField(max_length=500)
    image = models.ImageField(blank=True, upload_to='images')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
