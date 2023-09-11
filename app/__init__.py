from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
import psycopg2
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Govind31@localhost:5432/todoapp'
db = SQLAlchemy(app)




from app import routes, models

