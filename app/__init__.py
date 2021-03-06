from __future__ import absolute_import
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
import sys
import os


site = Flask(__name__)
site.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

if os.environ.get('FLASK_ENV') == 'development':
    site.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/devdb'
else:
    site.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

db = SQLAlchemy(site)
migrate = Migrate(site, db)
bootstrap = Bootstrap(site)

root_path = site.root_path
parent_path = '/'.join(root_path.split('/')[:-1]) + '/'
sys.path.insert(0, parent_path)
os.environ['PYTHONPATH']=parent_path

import app.models
import app.views
