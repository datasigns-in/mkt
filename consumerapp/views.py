from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import ConsumerProfile, Subscription, LoggingDetail

def register(request):
    if request.method == 'POST':
        # Handle user registration form submission
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username, email=email, password=password)
        consumer_profile = ConsumerProfile.objects.create(user=user, email=email)
        # Redirect to login page after successful registration
        return redirect('login')
    else:
        return render(request, 'register.html')

@login_required
def profile(request):
    user = request.user
    consumer_profile = ConsumerProfile.objects.get(user=user)
    return render(request, 'profile.html', {'consumer_profile': consumer_profile})

@login_required
def edit_profile(request):
    user = request.user
    consumer_profile = ConsumerProfile.objects.get(user=user)
    if request.method == 'POST':
        # Handle profile edit form submission
        consumer_profile.preferences = request.POST['preferences']
        consumer_profile.save()
        # Log the action
        LoggingDetail.objects.create(user=user, action='Profile updated')
        return redirect('profile')
    else:
        return render(request, 'edit_profile.html', {'consumer_profile': consumer_profile})

@login_required
def subscribe(request):
    if request.method == 'POST':
        # Handle subscription form submission
        subscription_id = request.POST['subscription']
        subscription = Subscription.objects.get(pk=subscription_id)
        user = request.user
        consumer_profile = ConsumerProfile.objects.get(user=user)
        consumer_profile.subscriptions.add(subscription)
        # Deduct subscription price from wallet balance
        consumer_profile.wallet_balance -= subscription.price
        consumer_profile.save()
        # Log the action
        LoggingDetail.objects.create(user=user, action=f'Subscribed to {subscription.name}')
        return redirect('profile')
    else:
        subscriptions = Subscription.objects.all()
        return render(request, 'subscribe.html', {'subscriptions': subscriptions})



# This views.py file defines the following views:

# register: Handles user registration.
# profile: Displays the user's profile.
# edit_profile: Allows users to edit their profile.
# subscribe: Handles subscription to different plans.
# Ensure to create corresponding HTML templates (register.html, profile.html, edit_profile.html, subscribe.html) for rendering the user interface of these views.
