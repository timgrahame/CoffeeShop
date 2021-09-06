import os
from os import environ as env
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
import json
from dotenv import load_dotenv

# load database environment details from .env

load_dotenv()
database_path = "postgres://{}:{}@{}/{}".format(
    env['DB_USER'],
    env['DB_PASSWORD'],
    env['DB_HOST'],
    env['DB_NAME']
    )

db = SQLAlchemy()

# setup database


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


def db_drop_and_create_all():
    db.drop_all()
    print("Database dropped")
    db.create_all()
    print("Database created")
    # add one demo row which is helping in POSTMAN test
    drink = Drink(
        title='water',
        recipe='[{"name": "water", "color": "blue", "parts": 1}]')
    drink.insert()


# Build the database model.

class Drink(db.Model):
    id = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)
    title = Column(String(80), unique=True)
    recipe = Column(String(180), nullable=False)

    # define short drink model

    def short(self):
        print(json.loads(self.recipe))
        short_recipe = [{
            'color': r['color'],
            'parts': r['parts']}
            for r in json.loads(self.recipe)]

        return {
            'id': self.id,
            'title': self.title,
            'recipe': short_recipe
        }

    # define long drink model

    def long(self):
        return {
            'id': self.id,
            'title': self.title,
            'recipe': json.loads(self.recipe)
        }

    # define insert function

    def insert(self):
        db.session.add(self)
        db.session.commit()

    # delete drink function

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # define update drink function

    def update(self):
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.short())
