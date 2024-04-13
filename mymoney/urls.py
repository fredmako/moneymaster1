# mymoney/urls.py

from django.urls import path
from . import views
from mymoney import views
urlpatterns = [
    path('home/', views.start, name='start'),  # Root URL pattern
    path('signup/', views.signup_start, name='signup_start'),
    path('signup/process/', views.signup_process, name='signup_process'),
    path('signup/success/', views.signup_success, name='signup_success'),
    # Other URL patterns for your app
]
