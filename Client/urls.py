from django.urls import path

from . import views

urlpatterns = [
    path("", views.clientsList, name="clientsList"),
    path("ClientCrud/", views.ClientCRUD, name='index'),
   
]
