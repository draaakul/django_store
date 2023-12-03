from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name
