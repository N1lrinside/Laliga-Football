from django.db import models

# Create your models here.
class Teams(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'team'
        verbose_name_plural = 'teams'

class Footballs(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=50)
    POS = models.CharField(max_length=50)
    PAC = models.IntegerField()
    SHO = models.IntegerField()
    PAS = models.IntegerField()
    DRI = models.IntegerField()
    DEF = models.IntegerField()
    PHY = models.IntegerField()
    id_club = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'football'
        verbose_name_plural = 'footballs'