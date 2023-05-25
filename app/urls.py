from django.contrib import admin
from django.urls import path

from django.urls import include 


from . import views #NEW

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("",views.home_view)
    path("",views.home_view_temp),
    path("about" , views.about_view_temp),
    path("coffee" ,views.coffee_view_temp) , 
    path("p2",views.p2_view_temp),
    path("sr",views.sr_view_temp) ,
    
    
]