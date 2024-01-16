from django.contrib import admin
from django.urls import path,include
from Home import views 
urlpatterns = [
    path("",views.home),
    path("show",views.show),
    path("sendemp",views.sendemp),
    path("senddept",views.senddept),
    path("deleteemp",views.deleteemp),
    path("editemp",views.editemp),
    path("deletedept",views.deletedept),
    path("editdept",views.editdept)
]
