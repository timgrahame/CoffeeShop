import os
from types import MethodDescriptorType
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS
from sqlalchemy.sql.expression import null

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

# Uncomment the line below on first run to create tables and introduce sample data.

## db_drop_and_create_all()

# Get Drinks Endpoint


@app.route('/drinks', methods=['GET'])
def get_drinks():
    try:
        drinks = Drink.query.all()
        return jsonify({
            'success': True,
            'drinks': [drink.short() for drink in drinks],
        }), 200

    except Exception as e:
        print("Exception is", e)
        abort(404)


# Get Drinks-detail Endpoint

@app.route('/drinks-detail', methods=['GET'])
@requires_auth('get:drinks-detail')
def get_drinks_detail(payload):
    try:
        drinks = Drink.query.all()
        return jsonify({
            'success': True,
            'drinks': [drink.long() for drink in drinks]
        }), 200

    except Exception as e:
        print("Exception is", e)
        abort(401)

# Post Drinks Endpoint


@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def post_drinks(payload):
    try:
        body = request.get_json()
        if body is None:
            abort(400)

        drink_title = body.get("title", None)
        drink_recipe = body.get("recipe", [])

        create_drink = Drink(
            title=drink_title,
            recipe=json.dumps(drink_recipe))
        print(drink_recipe)
        create_drink.insert()

        return jsonify({
            'success': True,
            'drinks': [create_drink.long()],
        }), 200

    except Exception as e:
        print("Exception is", e)
        abort(422)

# Patch Drinks/id endpoint


@app.route('/drinks/<int:id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def patch_drinks(payload, id):

    body = request.get_json()
    drink = Drink.query.filter(Drink.id == id).one_or_none()
    if body is None:
        abort(404)

    title = body.get("title", None)
    if title is not None:
        drink.title = title

    recipe = body.get("recipe", None)
    if recipe is not None:
        drink.recipe = json.dumps(recipe)

    drink.update()

    return jsonify({
        'success': True,
        'drinks': [drink.long()],
    }), 200

# Delete Drinks/id Endpoint


@app.route('/drinks/<int:id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drinks(payload, id):
    drink = Drink.query.get(id)
    if drink is None:
        print(drink)
        abort(404)
    drink.delete()

    return jsonify({
        'success': True,
        'drinks': [drink.long()],
    }), 200

# Error Handling


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@app.errorhandler(500)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": "Internal Server Error - The server wants to be awkward"
    }), 500


@app.errorhandler(400)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "Bad Request"
    }), 400


@app.errorhandler(404)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "Not Found"
    }), 404

# AuthError error handler


@app.errorhandler(AuthError)
def handle_auth_error(error):
    return jsonify({
        "success": False,
        "error": error.error["code"],
        "message": error.error["description"]
    }), error.status_code
