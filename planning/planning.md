# Project 4 Planning

My final project I will be making an app that displays the statistics of a specific game of NFL football. I would like to do analysis on the trends of the game as one of the displays and a cool visualization of the stats on another display. The App will be built with a React front end and a Django back end.

# Models

Team

- name
- stadium
- coach
- Players (list of players)

Player

- name
- number
- Team (FK to team)

Game

- date_time
- home_team (FK to team)
- away_team (FK to team)
- home_team_score
- away_team_score
- plays (list of plays)

Play

- play_number
- quarter
- time_at_start_of_play
- offensive_team
- defensive_team
- play_type (i.e running or passing etc.)
- result (net yardage)
- player (who gets the stats for the result)

These are the Models that I am thinking I will need for MVP. I plan to add much more detail to each model to do more detailed analysis if I have the time. I will update this planning file as I add more
