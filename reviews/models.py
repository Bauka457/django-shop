from django.db import models
from shop.models import Product

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    text = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.author} – {self.product}"
