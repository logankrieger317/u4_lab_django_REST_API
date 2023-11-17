from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    
    path('teams/', views.TeamsList.as_view(), name='team_list'),
    path('teams/<int:pk>/', views.TeamsDetail.as_view(), name='teams-detail'),
    path('players/', views.PlayersList.as_view(), name='player_list'),
    path('players/<int:pk>/', views.PlayersDetail.as_view(), name='players_detail'),
]