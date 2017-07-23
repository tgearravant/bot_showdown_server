from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from application import app
from database import db
import lib.models.player
import lib.models.bot
import lib.models.game
import lib.models.game_instance

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()