from uuid import UUID
from fastapi import APIRouter
from Application.PlayerActions import add_player, get_all_players, get_player_details, remove_player, update_player_elo
from Application.EloHelper import calculate_player_elo

router = APIRouter()

@router.get("/players")
def get_player():
    return get_all_players()

@router.get("/players/{player_id}")
def get_player(player_id):
    return get_player_details(player_id)

@router.post("/players")
def create_player(name):
    return add_player(name)

@router.delete("/players/{player_id}")
def delete_player(player_id: UUID):
    remove_player(player_id)
    return

@router.post("/Games")
def new_game(winner_player_id: UUID, loser_player_id: UUID):
    winner = get_player_details(winner_player_id)
    loser = get_player_details(loser_player_id)
    winner_elo = calculate_player_elo(winner.elo, loser.elo, 1)
    loser_elo = calculate_player_elo(loser.elo, winner.elo, 0)
    update_player_elo(winner.id, winner_elo)
    update_player_elo(loser.id, loser_elo)
    return