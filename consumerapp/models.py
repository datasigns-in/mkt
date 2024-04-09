from django.db import models
from django.contrib.auth.models import User

class ConsumerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    preferences = models.TextField(blank=True)
    subscriptions = models.ManyToManyField('Subscription', blank=True)
    wallet_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.user.username

class Subscription(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class LoggingDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.action}"

class Form(models.Model):
    consumer = models.ForeignKey(ConsumerProfile, on_delete=models.CASCADE)
    form_data = models.JSONField()

class Test(models.Model):
    consumer = models.ForeignKey(ConsumerProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    result = models.CharField(max_length=100)

class ModelSubscription(models.Model):
    consumer = models.ForeignKey(ConsumerProfile, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=100)
    subscribed_on = models.DateTimeField(auto_now_add=True)


# This models.py file defines the following models:

# ConsumerProfile: Stores consumer details like name, email, preferences, subscriptions, and wallet balance.
# Subscription: Represents different subscription plans available for consumers.
# LoggingDetail: Logs actions performed by consumers.
# Form: Stores form data submitted by consumers.
# Test: Stores test results for consumers.
# ModelSubscription: Tracks models subscribed to by consumers and when they subscribed.
# Feel free to customize these models further based on your specific requirements. Additionally, don't forget to run python manage.py makemigrations and python manage.py migrate after defining or modifying your models to apply the changes to your database schema.    
