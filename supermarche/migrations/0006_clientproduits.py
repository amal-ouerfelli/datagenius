# Generated by Django 3.0.8 on 2020-12-10 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supermarche', '0005_auto_20201206_1540'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientProduits',
            fields=[
                ('id_t', models.AutoField(db_column='id_T', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'client-produits',
                'managed': False,
            },
        ),
    ]