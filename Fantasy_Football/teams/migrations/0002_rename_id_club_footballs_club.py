# Generated by Django 5.0.4 on 2024-05-09 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='footballs',
            old_name='id_club',
            new_name='club',
        ),
    ]
