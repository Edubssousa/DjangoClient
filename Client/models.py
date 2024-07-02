from django.db import models

# Create your models here.

class Clients(models.Model):
    name = models.models.CharField(max_length=100)
    email = models.models.EmailField(unique=True, max_length=254)
    phone = models.models.CharField(max_length=20,blank=True)

    def __str__(self):
        return self.nome
