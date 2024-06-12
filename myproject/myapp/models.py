from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    images = models.ImageField(upload_to='upload',blank=True)

    def __str__(self):
        return self.name