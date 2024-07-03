from django.db import models

# Create your models here.


class Clients(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=254)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name
