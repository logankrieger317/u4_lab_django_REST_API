from rest_framework import serializers
from .models import Teams, Players

class PlayersSerializer(serializers.HyperlinkedModelSerializer):
    team = serializers.HyperlinkedRelatedField(
        view_name='teams-detail',
        read_only=True
    )
    
    team_id = serializers.PrimaryKeyRelatedField(
        queryset= Teams.objects.all(),
        source='team',
    )
    class Meta:
        model = Players
        fields = ('id', 'name', 'team', 'position', 'age','team_id', 'injury_reserve' )
        # fields = '__all__'
        
        
class TeamsSerializer(serializers.HyperlinkedModelSerializer):
    players = PlayersSerializer(
        many=True,
        read_only=True
    )
    
    team_url = serializers.ModelSerializer.serializer_url_field(
    view_name='players_detail'
    )
    
    class Meta:
       model = Teams
       fields = ('id', 'name', 'players', 'team_url')
       