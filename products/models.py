from django.db import models
from django.utils.text import slugify

from categories.models import Category


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name = 'products')

    class Meta:
        ordering = ["-created_at"]
        searching = ['name', 'category']

    def __str__(self):
        return self.name

    #slug logic, check if slug exist, if not generate from name and save normally
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            super().save(*args, **kwargs)

    def is_in_stock(self):
        return self.stock > 0

