from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Flower(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='flowers')
    image = models.ImageField(upload_to='flowers/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    country_of_origin = models.CharField(max_length=100)

    def __str__(self):
        return self.name