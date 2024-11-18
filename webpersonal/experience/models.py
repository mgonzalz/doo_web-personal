from django.db import models
import os
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.
class Experience(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="experiences")
    date_started = models.DateField()
    date_ended = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "experiencia"
        verbose_name_plural = "experiencias"
        ordering = ["-date_started"]
    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title


@receiver(post_delete, sender=Experience)
def delete_image_on_object_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
