# Generated by Django 3.0.8 on 2020-12-06 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supermarche', '0004_remove_client_somme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='price',
            field=models.CharField(max_length=255),
        ),
    ]
