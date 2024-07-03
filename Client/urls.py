from django.urls import path

from . import views

urlpatterns = [
    path("", views.addClient, name='index'),
    path("/listClients", views.listClients, name="listClients"),
    path("/detailsClient", views.detailsClient, name="detailsClient"),
    path("/updateClient", views.updateClient, name="updateClient"),
    path("/deleteClient", views.deleteClient, name="deleteClient"),
]
