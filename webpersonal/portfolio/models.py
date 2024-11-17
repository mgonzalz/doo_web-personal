from django.db import models
import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
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

    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title # Devuelve el título del proyecto como representación del objeto en la base de datos.




@receiver(post_delete, sender=Project)
def delete_image_on_object_delete(sender, instance, **kwargs):
    """
    Borra la imagen asociada cuando un objeto Project es eliminado.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):  # Verifica si la imagen existe en el sistema de archivos
            os.remove(instance.image.path)
