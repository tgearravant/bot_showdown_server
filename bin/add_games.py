# Run this after updating games_list.py or incrementing game versions to make sure that the appropriate game is in the database.

from lib.games.games_list import list_of_game_classes
from lib.models.game import Game
from database import db

code_names = iter(list_of_game_classes)
db_games = Game.query.all()

for code_name in code_names:
    game = Game(list_of_game_classes[code_name].NAME,
                list_of_game_classes[code_name].UUID,
                list_of_game_classes[code_name].REVISION_NUMBER,
                code_name)
    if any(game.equals(db_game) for db_game in db_games):
        continue
    db.session.add(game)
    db.session.commit()
