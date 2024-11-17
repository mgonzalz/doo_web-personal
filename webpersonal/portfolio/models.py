from django.db import models

# Create your models here.
'''
Representa una tabla dentro de la base de datos. Cada clase representa una tabla. Se deberán
de crear las columnas de la tabla. Cada columna será un atributo de la clase.
'''
class Project(models.Model): # Hereda de models.Model. El nombre SIEMPRE en singular.
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
