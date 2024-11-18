from django.shortcuts import render
from .models import Experience
# Create your views here.
def experiences(request):
    experiences = Experience.objects.all() # Recuperar todos los proyectos de la base de datos
    return render(request, "experiences/experiences.html", {'experiences': experiences}) # Enviar los proyectos al template
