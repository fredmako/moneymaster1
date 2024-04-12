from django.urls import path
from . import views  # Assuming views.py is in the current app directory

app_name = 'mymoney'  # Define the namespace name

urlpatterns = [
  path('start/', views.signup_start, name='start'),
  path('', views.signup_process, name='signup_process'),
  # ... other URL patterns for your mymoney app
]
