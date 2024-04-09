# views.py in the marketplace app

from django.shortcuts import render
from .models import ModelProject

def model_list(request):
    models = ModelProject.objects.all()
    return render(request, 'marketplace/model_list.html', {'models': models})

def model_detail(request, model_id):
    model = ModelProject.objects.get(id=model_id)
    return render(request, 'marketplace/model_detail.html', {'model': model})
