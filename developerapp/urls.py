from django.urls import path
from . import views

app_name = 'developer'

urlpatterns = [
    path('model-projects/', views.model_project_list, name='model_project_list'),
    path('model-projects/<int:pk>/', views.model_project_detail, name='model_project_detail'),
    path('subscriptions/', views.subscription_list, name='subscription_list'),
    path('model-pricings/', views.model_pricing_list, name='model_pricing_list'),
    path('developer-balance/', views.developer_balance, name='developer_balance'),
]
