import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from .models import MinPanier
from .serializers import MinPanierSerializer


# initialize the APIClient app
client = Client()



class GetAllClientsTest(TestCase):
    """ Test module for GET all clients API """

    def setUp(self):
        MinPanier.objects.create(
            id_p=2, quantite=14)
        MinPanier.objects.create(
            id_p=3, quantite=15)
        MinPanier.objects.create(
            id_p=1, quantite=2)
        MinPanier.objects.create(
            id_p=2, quantite=8)

    def test_get_all_clients(self):
        # get API response
        response = client.get(reverse('mon_panier'))
        # get data from db
        paniers = MinPanier.objects.all()
        serializer = MinPanierSerializer(paniers, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)