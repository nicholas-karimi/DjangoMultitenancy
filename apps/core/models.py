from django.db import models

from colorfield.fields import ColorField

class Item(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class SiteSettings(models.Model):
    name = models.CharField(max_length=255)
    color = ColorField(default='#000000')
    logo = models.ImageField(upload_to='logo/', null=True, blank=True)

    def __str__(self):
        return self.name