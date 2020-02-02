from __future__ import absolute_import
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
import sys
import os


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/devdb'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)

root_path = app.root_path
parent_path = '/'.join(root_path.split('/')[:-1]) + '/'
sys.path.insert(0, parent_path)
os.environ['PYTHONPATH']=parent_path

import personal_site.models
import personal_site.views
