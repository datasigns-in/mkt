from django.db import models
from django.contrib.auth.models import User

class Subscription(models.Model):
    consumer = models.ForeignKey(User, on_delete=models.CASCADE)
    developer = models.ForeignKey(User, related_name='developer_subscriptions', on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()

class ModelPricing(models.Model):
    developer = models.ForeignKey(User, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class DeveloperBalance(models.Model):
    developer = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

class ModelProject(models.Model):
    developer = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    training_dataset = models.FileField(upload_to='datasets/')
    test_dataset = models.FileField(upload_to='datasets/')
    trained_model = models.FileField(upload_to='trained_models/', blank=True, null=True)
    evaluation_result = models.TextField(blank=True, null=True)
    deployment_status = models.BooleanField(default=False)

class ModelFeatureUsage(models.Model):
    model_project = models.ForeignKey(ModelProject, on_delete=models.CASCADE)
    feature_name = models.CharField(max_length=100)
    usage_count = models.IntegerField(default=0)
