# Generated by Django 3.0.8 on 2020-12-06 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supermarche', '0003_auto_20201206_1357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='somme',
        ),
    ]
