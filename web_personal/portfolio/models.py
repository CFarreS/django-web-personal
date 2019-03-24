from django.db import models


# Create your models here.
class Project(models.Model):
    """ Model per agregar projectes a la base de dades """
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

