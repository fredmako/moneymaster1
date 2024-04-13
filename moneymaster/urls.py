

from django.contrib import admin
from django.urls import path, include
import mymoney.views as mymoney_views  # Import mymoney.views with an alias
urlpatterns = [
  path('admin/', admin.site.urls),
  path('', mymoney_views.start, name='root'),  # Root URL pattern

  path('mymoney/', include('mymoney.urls')),  # Include mymoney app's URLs with namespace prefix
  # ... other URL patterns for your project
]
