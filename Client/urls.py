from django.urls import path

from . import views

urlpatterns = [
    path("", views.clientsList, name="clientsList"),
    path("ClientCrud/<int:pk>/", views.ClientCRUD, name='index'),# testar o pk que talvez seja id
   
]
