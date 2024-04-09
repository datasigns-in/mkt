from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ModelProject, Subscription, ModelPricing, DeveloperBalance, ModelFeatureUsage

@login_required
def model_project_list(request):
    model_projects = ModelProject.objects.filter(developer=request.user)
    return render(request, 'developer/model_project_list.html', {'model_projects': model_projects})

@login_required
def model_project_detail(request, pk):
    model_project = ModelProject.objects.get(pk=pk)
    return render(request, 'developer/model_project_detail.html', {'model_project': model_project})

@login_required
def subscription_list(request):
    subscriptions = Subscription.objects.filter(developer=request.user)
    return render(request, 'developer/subscription_list.html', {'subscriptions': subscriptions})

@login_required
def model_pricing_list(request):
    model_pricings = ModelPricing.objects.filter(developer=request.user)
    return render(request, 'developer/model_pricing_list.html', {'model_pricings': model_pricings})

@login_required
def developer_balance(request):
    developer_balance = DeveloperBalance.objects.get(developer=request.user)
    return render(request, 'developer/developer_balance.html', {'developer_balance': developer_balance})


# These views handle listing and displaying details of model projects, subscriptions, model pricings, and developer balance for the authenticated developer user. Make sure to create corresponding HTML templates for these views in the developer app templates directory.
