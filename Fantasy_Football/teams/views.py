from django.shortcuts import render
from .models import Teams, Footballers, Countries
def ur_teams(request):
    return render(request, 'teams/ur_teams.html')

def real_fc(request):
    if request.method == 'POST':
        team_name = request.POST.get('team')
        transfer_from = request.POST.get('team_transfer')
        if team_name:
            footballers = Footballers.objects.filter(club=team_name)
        if transfer_from:
            transfers = Footballers.objects.filter(club=transfer_from)
    else:
        footballers = Footballers.objects.filter(id=0)
        transfers = Footballers.objects.all()
    teams = Teams.objects.all()
    return render(request, 'teams/real_fc.html', {'teams': teams, 'footballers': footballers, 'transfers': transfers})