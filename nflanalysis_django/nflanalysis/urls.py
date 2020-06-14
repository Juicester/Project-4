# nflanalysis/urls.py

from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('teams', views.TeamList.as_view(), name='team_list'),
    path('teams/<int:pk>', views.TeamDetail.as_view(), name='team_detail'),
    path('games/', views.GameList.as_view(), name="game_list"),
    path('games/<int:pk>', views.GameDetail.as_view(), name="game_detail"),
]
