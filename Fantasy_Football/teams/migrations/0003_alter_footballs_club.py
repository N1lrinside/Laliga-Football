# Generated by Django 5.0.4 on 2024-05-10 12:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_rename_id_club_footballs_club'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footballs',
            name='club',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.teams'),
        ),
    ]
