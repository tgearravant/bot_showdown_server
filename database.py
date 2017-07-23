from application import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

involved_bots = db.Table('involved_bots',
                         db.Column('bot_id', db.Integer, db.ForeignKey('bot.id'), nullable = False),
                         db.Column('game_instance_id', db.Integer, db.ForeignKey('game_instance.id'), nullable = False)
                         )