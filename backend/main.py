from fastapi import FastAPI
from nba import get_todays_games

app = FastAPI()

@app.get("/")
async def root():
    return {
        "message" : "Hello Keyanna"
    }

game = {
    "game_id": 1,
    "live_status": 2,
    "home_team": "Celtics",
    "away_team": "76ers",
    "arena": "TD Garden",
    "game_type": "Playoff"
}

@app.get("/games/{game_id}")
async def read_game(game_id: int):
    return game

@app.get("/games")
async def read_games():
    games = get_todays_games()
    return games