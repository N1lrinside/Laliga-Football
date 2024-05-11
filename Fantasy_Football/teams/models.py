from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.
class Teams(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'team'
        verbose_name_plural = 'Команды'

class Countries(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.country

    class Meta:
        verbose_name = 'country'
        verbose_name_plural = 'Страны'

class Footballers(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=50)
    country = models.ForeignKey(Countries, on_delete=models.CASCADE, db_column='country')
    club = models.ForeignKey(Teams, on_delete=models.CASCADE, db_column='club')
    POS = models.CharField(max_length=4)
    rating = models.IntegerField(validators=[MaxValueValidator(99)])
    PAC = models.IntegerField(validators=[MaxValueValidator(99)])
    SHO = models.IntegerField(validators=[MaxValueValidator(99)])
    PAS = models.IntegerField(validators=[MaxValueValidator(99)])
    DRI = models.IntegerField(validators=[MaxValueValidator(99)])
    DEF = models.IntegerField(validators=[MaxValueValidator(99)])
    PHY = models.IntegerField(validators=[MaxValueValidator(99)])

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'football'
        verbose_name_plural = 'Футболисты'