from django.contrib.auth.models import User
from django.db import models


# Create your models here.

# Секој оглас се карактеризира со наслов,
# опис, време и датум на постирање, категорија на оглас,
# корисникот кој го креирал огласот, фотографија од продуктот,
# цена, статус (цената е фиксна, прифаќам предлози, цената не е фиксна)
# и информација за тоа дали е нов или не е.


# За секоја категорија се чува име, опис, датум на креирање,
# информација за тоа дали се работи за недвижнини.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    creationDate = models.DateField()
    isRealEstate = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Listing(models.Model):
    STATUS_CHOICES = [
        ('fixed-price', 'Fixed price'),
        ('variable-price', 'Variable price')
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    datetime = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='fixed-price')
    isNewListing = models.BooleanField('Is new Listing', default=False)

    def __str__(self):
        return f"{self.title} - {self.category.name}"
