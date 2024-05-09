from django.urls import path
from . import views

urlpatterns = [
    path('ur_teams/', views.ur_teams, name = 'fantasy-team'),
    path('real_fc', views.real_fc, name = 'real-team')
]
