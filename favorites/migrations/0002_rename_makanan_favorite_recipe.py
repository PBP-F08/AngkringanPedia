# Generated by Django 5.0.6 on 2024-10-27 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('favorites', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favorite',
            old_name='makanan',
            new_name='recipe',
        ),
    ]