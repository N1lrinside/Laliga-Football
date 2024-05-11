# Generated by Django 5.0.4 on 2024-05-10 16:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0006_footballs_club'),
    ]

    operations = [
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'country',
                'verbose_name_plural': 'Страны',
            },
        ),
        migrations.AddField(
            model_name='footballs',
            name='rating',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(99)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='footballs',
            name='DEF',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99)]),
        ),
        migrations.AlterField(
            model_name='footballs',
            name='DRI',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99)]),
        ),
        migrations.AlterField(
            model_name='footballs',
            name='PAC',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99)]),
        ),
        migrations.AlterField(
            model_name='footballs',
            name='PAS',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99)]),
        ),
        migrations.AlterField(
            model_name='footballs',
            name='PHY',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99)]),
        ),
        migrations.AlterField(
            model_name='footballs',
            name='POS',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='footballs',
            name='SHO',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99)]),
        ),
    ]
