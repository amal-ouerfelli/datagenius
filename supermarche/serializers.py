from rest_framework import serializers 
from .models import Produit, Client, ClientProduits, MinPanier

class ProduitsSerializer (serializers.ModelSerializer): 
    class Meta : 
        model = Produit
        fields = ['id_p', 'price', 'name', 'id_offre']

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model= Client
        fields="__all__"

class ClientProduitsSerializer(serializers.ModelSerializer):
    class Meta:
        model=ClientProduits
        fields="__all__"

class MinPanierSerializer(serializers.ModelSerializer):
    class Meta:
        model=MinPanier
        fields="__all__"