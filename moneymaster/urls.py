
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  path('admin/', admin.site.urls),
  path('mymoney/', include('mymoney.urls', namespace='mymoney')),  # Include mymoney app's URLs with namespace prefix
  # ... other URL patterns for your project
]
