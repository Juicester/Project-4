from rest_framework import serializers
from .models import Team, Game


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    home_team = serializers.HyperlinkedRelatedField(
        view_name='game_detail',
        many=True,
        read_only=True
    )
    away_team = serializers.HyperlinkedRelatedField(
        view_name='game_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Team
        fields = ('id', 'team_name', 'conference', 'division', 'wins', 'losses', 'ties', 'points_for', 'points_against', 'rush_td', 'pass_td',
                  'total_td', 'pass_yards', 'rush_yards', 'int_for', 'forced_fumbles', 'fumbles_recovered', 'sacks', 'fumble_td', 'int_td', 'safeties', 'home_team', 'away_team')


class GameSerializer(serializers.HyperlinkedModelSerializer):
    home_team = serializers.HyperlinkedRelatedField(
        view_name='team_detail',
        read_only=True
    )
    away_team = serializers.HyperlinkedRelatedField(
        view_name='team_detail',
        read_only=True
    )

    class Meta:
        model = Game
        fields = ('game_id', 'week', 'day', 'date', 'away_team', 'away_spread',
                  'home_team', 'home_spread', 'over_under', 'away_score', 'home_score',)
