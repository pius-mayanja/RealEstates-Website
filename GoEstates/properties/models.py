from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


PROPERTY_CATEGORIES = (('Single-Family Home','Single-Family Home'),
                       ('Condominium','Condominium'),
                       ('TownHouse','TownHouse'), 
                       ('Apartment','Apartment'),
                       ('Duplex','Duplex'),
                       ('Triplex','Triplex'),
                       ('Vaccant-Land','Vaccant-Land'),
                       ('Commercial Property','Commercial Property'),
                       ('Industrial Property','Industrial Property'),
                       ('Agricultural Property','Agricultural Property'),
                       ('Mixed-Use Property','Mixed-Use Property'),
                       ('TimeShare','TimeShare'),
                       ('Cooperative','Cooperative'), 
                       ('Mobile Home','Mobile Home'),
)

PROPERTY_CONDITIONS = (
    ('Brand New', 'Brand New'),
    ('Renovated', 'Renovated'),
    ('Fixer-Upper','Fixed-Upper'),
    ('Luxury','Luxury'),
    ('Furnished','Furnished'),
)


class Category(models.Model):
    name = models.CharField(max_length=100, choices=PROPERTY_CATEGORIES)
    description = models.TextField(blank=False)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Property(models.Model):
    category = models.ForeignKey(Category, related_name='property',on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=False)
    image = models.ImageField(upload_to='images/', null=True)
    price = models.DecimalField(decimal_places=2,max_digits=20)
    location = models.CharField(max_length=100)
    bedrooms = models.IntegerField(blank=True)
    bathrooms = models.IntegerField(blank=True)
    sqft = models.IntegerField()
    condition = models.CharField(max_length=100, choices = PROPERTY_CONDITIONS, default='Brand New')
    date = models.DateField(null=True, auto_now=True)
    property_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'

    def __str__(self):
        return self.name
    

class PropertyImages(models.Model):
    property = models.ForeignKey(Property, related_name="property_image", on_delete=models.CASCADE)
    property_image = models.ImageField(upload_to='property_images/')

    class Meta:
        verbose_name = 'PropertyImages'
        verbose_name_plural = 'PropertyImages'

    def __str__(self) -> str:
        return f"Image for {self.property.name}"

class Videos(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE)
    video = models.FileField(upload_to='videos/')

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

    def __str__(self):
        return f"Video for {self.property.name}"