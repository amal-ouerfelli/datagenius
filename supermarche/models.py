from django.db import models


class Offre(models.Model):
    id_offre = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'offre'


class Produit(models.Model):
    id_p = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    id_offre = models.ForeignKey(Offre, models.DO_NOTHING, db_column='id_offre')

    class Meta:
        db_table = 'produit'


class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    nomprenom = models.CharField(max_length=250)
    carte_fidelite = models.CharField(max_length=250)
    

    class Meta:
        db_table = 'client'

class ClientProduits(models.Model):
    id_t = models.AutoField(db_column='id_T', primary_key=True)  # Field name made lowercase.      
    id_client = models.ForeignKey(Client, models.DO_NOTHING, db_column='id_client')
    id_p = models.ForeignKey('Produit', models.DO_NOTHING, db_column='id_p')
    somme=models.IntegerField()

    class Meta:
        managed = False
        db_table = 'client-produits'

class MinPanier(models.Model):
    id_panier = models.AutoField(primary_key=True)
    id_p = models.ForeignKey('Produit', models.DO_NOTHING, db_column='id_p')
    quantité=models.IntegerField()

    class Meta:
        managed = False
        db_table = 'min_panier'