# Generated by Django 5.1.4 on 2024-12-18 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_favorite'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Favorite',
        ),
    ]