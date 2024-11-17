from django.db import models

# Create your models here.
'''
Representa una tabla dentro de la base de datos. Cada clase representa una tabla. Se deberán
de crear las columnas de la tabla. Cada columna será un atributo de la clase.
'''
class Project(models.Model): # Hereda de models.Model. El nombre SIEMPRE en singular.
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    link = models.URLField(null=True, blank=True, verbose_name="Dirección web")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"] # Ordena los proyectos por fecha de creación de forma descendente.
    def __str__(self):
        return self.title # Devuelve el título del proyecto como representación del objeto en la base de datos.
