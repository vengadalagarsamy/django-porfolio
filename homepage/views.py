from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all() # turns database values into Python objects and passes to template
    return render(request, 'homepage/home.html', {'projects': projects})