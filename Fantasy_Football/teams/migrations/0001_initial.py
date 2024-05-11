# Generated by Django 5.0.4 on 2024-05-09 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Footballs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=50)),
                ('POS', models.CharField(max_length=50)),
                ('PAC', models.IntegerField()),
                ('SHO', models.IntegerField()),
                ('PAS', models.IntegerField()),
                ('DRI', models.IntegerField()),
                ('DEF', models.IntegerField()),
                ('PHY', models.IntegerField()),
                ('id_club', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'football',
                'verbose_name_plural': 'Футболисты',
            },
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('country', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'team',
                'verbose_name_plural': 'Команды',
            },
        ),
    ]