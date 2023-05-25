from django.contrib import admin
from django.urls import path

from django.urls import include 


from . import views #NEW

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.home_view)
]