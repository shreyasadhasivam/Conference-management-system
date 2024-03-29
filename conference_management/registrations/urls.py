from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_attendee, name='register_attendee'),
    path('registration-success/', views.registration_success, name='registration_success'),
]
