from django.shortcuts import render
from .models import Project


# Create your views here.
def portafolio(request):
    """ Injecció de dades de la base de dades als templates """
    projects = Project.objects.all()
    return render(request, 'portfolio/portafolio.html', {'projects': projects})
