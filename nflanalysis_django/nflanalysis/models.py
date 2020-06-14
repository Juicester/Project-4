from django.db import models

# Create your models here.


class Team(models.Model):
    team_name = models.CharField(max_length=100)
    conference = models.CharField(max_length=100)
    division = models.CharField(max_length=100)
    wins = models.CharField(max_length=10)
    losses = models.CharField(max_length=10)
    ties = models.CharField(max_length=10)
    points_for = models.CharField(max_length=10)
    points_against = models.CharField(max_length=10)
    rush_td = models.CharField(max_length=10)
    pass_td = models.CharField(max_length=10)
    total_td = models.CharField(max_length=10)
    pass_yards = models.CharField(max_length=10)
    rush_yards = models.CharField(max_length=10)
    int_for = models.CharField(max_length=10)
    forced_fumbles = models.CharField(max_length=10)
    fumbles_recovered = models.CharField(max_length=10)
    sacks = models.CharField(max_length=10)
    fumble_td = models.CharField(max_length=10)
    int_td = models.CharField(max_length=10)
    safeties = models.CharField(max_length=10)

    def __str__(self):
        return self.team_name


class Game(models.Model):
    game_id = models.CharField(max_length=10)
    week = models.CharField(max_length=10)
    day = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    away_team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name='away_team')
    away_spread = models.CharField(max_length=10)
    home_team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name='home_team')
    home_spread = models.CharField(max_length=10)
    over_under = models.CharField(max_length=10)
    away_score = models.CharField(max_length=10)
    home_score = models.CharField(max_length=10)

    def __str__(self):
        return (f"{self.away_team} @ {self.home_team}")
