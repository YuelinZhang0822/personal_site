from __future__ import absolute_import
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/devdb'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)

import logging
logger = logging.getLogger(__name__)
import os
import sys
print(os.environ['PYTHONPATH'])
logger.info("pythonpath: " + os.environ['PYTHONPATH'])
logger.info("sys path: " + sys.path)

import personal_site.models
import personal_site.views
