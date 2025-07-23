from datetime import datetime, timezone
from sqlmodel import Session, or_, select
from Domain.Games import Games
from Infrastructure.db import engine

def add_new_game(winner_player_id, loser_player_id):
    with Session(engine) as session:
        game = Games(winner_id=winner_player_id, loser_id=loser_player_id, date=datetime.now(timezone.utc))
        session.add(game)
        session.commit()

def get_player_game_history(player_id):
    with Session(engine) as session:
        query = select(Games).where(or_(Games.winner_id == player_id, Games.loser_id == player_id)).order_by(Games.date.desc()).limit(20)
        result = session.exec(query)
        
        return result.all()