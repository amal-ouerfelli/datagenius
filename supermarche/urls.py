from django.urls import path, include
from . import views


 
urlpatterns = [
    path('panier/', views.addPanier),
    path('list_produits', views.show_list_produits),
    path('client_produits', views.produit_client),
    path('min_panier', views.mon_panier),
    path('somme', views.Somme),
    path('detail_panier', views.MonPanierApi.as_view()),
    path('addPanier', views.addPanier)
   
]