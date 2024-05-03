from django.contrib import admin
from django.urls import path
from django.urls import path, re_path
from mymoney import views
from mymoney.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^get_chain$', views.get_chain, name="get_chain"),
    re_path('^mine_block$', views.mine_block, name="mine_block"),
    re_path('^is_valid$', views.is_valid, name="is_valid"),
]