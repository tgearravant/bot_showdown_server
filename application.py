from flask import Flask

from conf import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

import lib.routing.rest
import lib.routing.html