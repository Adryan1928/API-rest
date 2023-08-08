from rest_framework import viewsets, routers, serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
            model = Cliente
            fields = ('id', 'nome', 'endereco', 'idade')
