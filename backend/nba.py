# access file to nba_api
from nba_api.live.nba.endpoints import scoreboard, boxscore



def get_todays_games():
    games = scoreboard.ScoreBoard()
    return games.get_json()
