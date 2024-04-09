from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('subscribe/', views.subscribe, name='subscribe'),
]


# Make sure to include this urls.py file in the consumer app's main urls.py file using the include() function. This will ensure that these URLs are properly routed to the corresponding views when requested.
