from django.shortcuts import render
from .models import Project # Referencia al modelo para recuperar los proyectos y enviarlos al template

# Create your views here.
def portfolio(request):
    projects = Project.objects.all() # Recuperar todos los proyectos de la base de datos
    return render(request, "portfolio/portfolio.html", {'projects': projects}) # Enviar los proyectos al template
