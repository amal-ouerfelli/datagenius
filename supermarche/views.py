from rest_framework.views import APIView 
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import Http404, JsonResponse
from .serializers import ProduitsSerializer, ClientSerializer, ClientProduitsSerializer, MinPanierSerializer
from rest_framework.response import Response
from .models import Produit, Client, Offre, ClientProduits,MinPanier
from rest_framework import generics
from django.test import TestCase, Client
from django.urls import reverse

@api_view(['GET'])
def show_list_produits (request): #afficher la liste des produits
    if (request.method=="GET"):
        r1=Produit.objects.all() #renvoie de tous les objets de la table produit de la base de données
        r2=ProduitsSerializer(r1, many=True ) #serialisation des données
        return Response (r2.data)
    

@api_view(['GET','POST'])
def addPanier(request):
    if (request.method=="GET"):
        r1=Client.objects.all() #renvoie de tous les objets de la table client de la base de données
        r2=ClientSerializer(r1, many=True ) #serialisation des données
        return Response (r2.data)
    elif (request.method=="POST"):
        serializers=ClientSerializer(data=request.data) #serialisation des données saisies
        if (serializers.is_valid()):
            serializers.save()
            return Response(serializers.data, status=200) # retourne reponse json 

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)



class MonPanierApi(generics.CreateAPIView):
    queryset = MinPanier.objects.all() #renvoie de tous les objets de la table min_panier de la base de données
    serializer_class = MinPanierSerializer #serialisation des données
    

# Produit_client
@api_view(['GET','POST'])
def produit_client(request):
    if (request.method=="GET"):
        r1=ClientProduits.objects.all() #renvoie de tous les objets de la table client de la base de données
        r2=ClientProduitsSerializer(r1, many=True ) #serialisation des données
        return Response (r2.data)
    elif (request.method=="POST"):
        serializers=ClientProduitsSerializer(data=request.data) #serialisation des données saisies
        if (serializers.is_valid()):
            serializers.save()
            return Response(serializers.data, status=200) # retourne reponse json 

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def mon_panier(request):
    if (request.method=="GET"):
        r1=MinPanier.objects.all()  #renvoie de tous les objets de la table min_panier de la base de données
        r2=MinPanierSerializer(r1, many=True ) #serialisation des données
        return Response (r2.data)
    elif (request.method=="POST"):
        serializers=MinPanierSerializer(data=request.data) #serialisation des données saisies
        if (serializers.is_valid()):
            serializers.save()
            return Response(serializers.data, status=200) # retourne reponse json 

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def Somme(request):
    list_id_p_panier=[]
    list_quantite=[]
    list_price=[]
    list_id_p=[]
    som=0
    if (request.method=="GET"):
        r1=MinPanier.objects.all() #renvoie de tous les objets de la table min_panier de la base de données
        r2=MinPanierSerializer(r1, many=True ) #serialisation des données
        r11=Produit.objects.all()  #renvoie de tous les objets de la table produit de la base de données
        r22=ProduitsSerializer(r11, many=True ) #serialisation des données
        for i in range (len(r1)):
            list_quantite.append(r2.data[i]['quantité']) # ajouter les valeurs de la colonne quantité dans la liste list_quantite
            list_id_p_panier.append(r2.data[i]['id_p']) # ajouter les valeurs de la colonne id_p du table min_panier dans la liste list_id_p_panier
        for j in range(len(r11)):
            list_price.append(r22.data[j]['price']) # ajouter les valeurs de la colonne price dans la liste list_price
            list_id_p.append(r22.data[j]['id_p']) # ajouter les valeurs de la colonne id_p de la table produit dans la liste list_id_p
        for k in range(len(list_id_p_panier)):
            m=list_id_p.index(list_id_p_panier[k]) # chercher l'indice de l'id du produit
            # calcul de la somme
            if r22.data[m]['id_offre']==1:
                som=som+(int(list_price[m])*int(list_quantite[k]))
            elif r22.data[m]['id_offre']==2:
                som=som+((int(list_price[m])/2)*int(list_quantite[k]))
            else:
                som=som+((int(list_price[m])*int(list_quantite[k]))-int(list_price[m])*(int(list_quantite[k])%3))

    return Response (som)



