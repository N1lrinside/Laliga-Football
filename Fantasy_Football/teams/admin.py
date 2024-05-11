from django.contrib import admin
from .models import Teams, Footballers, Countries
# Register your models here.

admin.site.register(Teams)
admin.site.register(Footballers)
admin.site.register(Countries)