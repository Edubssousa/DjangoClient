from rest_framework import serializers
from .models import Clients

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ['name','email','phone']