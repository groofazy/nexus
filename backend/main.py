from fastapi import FastAPI

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

games = [
    {
        "game_id": 1,
        "live_status": 2,
        "home_team": "Celtics",
        "away_team": "76ers",
        "arena": "TD Garden",
        "game_type": "Playoff"
    },
    {
        "game_id": 2,
        "live_status": 1,
        "home_team": "Lakers",
        "away_team": "Warriors",
        "arena": "Crypto.com Arena",
        "game_type": "Playoff"
    }
]

@app.get("/games")
async def read_games():
    return games