from sqlmodel import Session, select
from Domain.Player import Player
from Infrastructure.db import engine

def add_player(player_name):
    with Session(engine) as session:
        player = Player(name=player_name, elo=1000, played_games=0)
        session.add(player)
        session.commit()

def update_player_elo(player_id, new_elo):
    with Session(engine) as session:
        query = select(Player).where(Player.id == player_id)
        result = session.exec(query)
        player = result.one_or_none()

        if player:
            player.elo = new_elo
            session.commit()
        else:
            print(f"Player with id {player_id} was not found.")

def change_player_name(player_id, player_name):
    with Session(engine) as session:
        query = select(Player).where(Player.id == player_id)
        result = session.exec(query)
        player = result.one_or_none()
        
        if player:
            player.name = player_name
            session.commit()
        else:
            print(f"Player with id {player_id} was not found.")

def get_all_players():
    with Session(engine) as session:
        query = select(Player)
        result = session.exec(query)
        
        return result.all()
    
def get_player_details(player_id):
    with Session(engine) as session:
        query = select(Player).where(Player.id == player_id)
        result = session.exec(query)
        player = result.one_or_none()

        if player:
            return player
        else:
            print(f"Player with id {player_id} was not found.")
            return None
    
def remove_player(player_id):
    with Session(engine) as session:
        query = select(Player).where(Player.id == player_id)
        result = session.exec(query)
        player = result.one_or_none()

        if player:
            session.delete(player)
            session.commit()
        else:
            print(f"Player with id {player_id} was not found.")

