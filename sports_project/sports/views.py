from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from .serializers import TeamsSerializer, PlayersSerializer
from .models import Teams, Players
# Create your views here.

class TeamsList(generics.ListCreateAPIView):
    queryset = Teams.objects.all()
    serializer_class = TeamsSerializer

class TeamsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teams.objects.all()
    serializer_class = TeamsSerializer
    
class PlayersList(generics.ListCreateAPIView):
    queryset = Players.objects.all()
    serializer_class = PlayersSerializer
    
class PlayersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Players.objects.all()
    serializer_class = PlayersSerializer
