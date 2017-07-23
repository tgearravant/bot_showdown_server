from flask import Flask
from flask_bcrypt import Bcrypt

from config.conf import DevelopmentConfig

configObject = DevelopmentConfig
app = Flask(__name__,static_url_path=configObject.STATIC_URL_PATH, static_folder=configObject.STATIC_FOLDER, template_folder = configObject.TEMPLATE_FOLDER)
app.config.from_object(configObject)

bcrypt = Bcrypt(app)

import lib.routing.html
import lib.routing.rest

