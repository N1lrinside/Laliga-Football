from django.shortcuts import render
from .models import Teams

def ur_teams(request):
    return render(request, 'teams/ur_teams.html')

def real_fc(request):
    teams = Teams.objects.all()
    return render(request, 'teams/real_fc.html', {'teams': teams})