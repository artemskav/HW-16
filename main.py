import json

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from utils import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
app.url_map.strict_slashes = False
db = SQLAlchemy(app)

@app.route("/users", methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        user = User.query.all()
        user_response = []
        for item in user:
            user_response.append({"id": item.id,
                                  "first_name": item.first_name,
                                  "last_name": item.last_name,
                                  "age": item.age,
                                  "email": item.email,
                                  "role": item.role,
                                  "phone": item.phone})
        return jsonify(user_response)
    elif request.method == 'POST':
        if isinstance(request.json, list):
            load_users_json(request.json)
        elif isinstance(request.json, dict):
            load_users_json([request.json])
        else:
            print("Неправильный тип данных")
        return jsonify(request.json)

@app.route("/users/<int:uid>", methods=['GET', 'PUT', 'DELETE'])
def get_user(uid):
    if request.method == 'GET':
        user = User.query.get(uid)
        return jsonify({"id": user.id,
                      "first_name": user.first_name,
                      "last_name": user.last_name,
                      "age": user.age,
                      "email": user.email,
                      "role": user.role,
                      "phone": user.phone})
    elif request.method == 'PUT':
        order = update_user(request.json, uid)
        return jsonify(order)
    elif request.method == 'DELETE':
        some_delete(User, uid)
        return ('OK')


@app.route("/orders", methods=['GET', 'POST'])
def get_orders():
    if request.method == 'GET':
        order = Order.query.all()
        order_response = []
        for item in order:
            order_response.append({"id": item.id,
                                "name": item.name,
                                "description": item.description,
                                "start_date": item.start_date,
                                "end_date": item.end_date,
                                "address": item.address,
                                "price": item.price,
                                "customer_id": item.customer_id,
                                "executor_id": item.executor_id})
        return jsonify(order_response)
    elif request.method == 'POST':
        if isinstance(request.json, list):
            load_orders_json(request.json)
        elif isinstance(request.json, dict):
            load_orders_json([request.json])
        else:
            print("Неправильный тип данных")
        return jsonify(request.json)


@app.route("/orders/<int:uid>", methods=['GET', 'PUT', 'DELETE'])
def get_order(uid):
    if request.method == 'GET':
        order = Order.query.get(uid)
        return jsonify({"id": order.id,
                        "name": order.name,
                        "description": order.description,
                        "start_date": order.start_date,
                        "end_date": order.end_date,
                        "address": order.address,
                        "price": order.price,
                        "customer_id": order.customer_id,
                        "executor_id": order.executor_id}
                       )
    elif request.method == 'PUT':
        order = update_order(request.json, uid)
        return jsonify(order)
    elif request.method == 'DELETE':
        some_delete(Order, uid)
        return ('OK')


@app.route("/offers", methods=['GET', 'POST'])
def get_offers():
    if request.method == 'GET':
        offer = Offer.query.all()
        offer_response = []
        for item in offer:
            offer_response.append({"id": item.id,
                                   "order_id": item.order_id,
                                   "executor_id": item.executor_id})
        return jsonify(offer_response)
    elif request.method == 'POST':
        if isinstance(request.json, list):
            load_offers_json(request.json)
        elif isinstance(request.json, dict):
            load_offers_json([request.json])
        else:
            print("Неправильный тип данных")

        return jsonify(request.json)


@app.route("/offers/<int:uid>", methods=['GET', 'PUT', 'DELETE'])
def get_offer(uid):
    if request.method == 'GET':
        offer = Offer.query.get(uid)
        return jsonify({"id": offer.id,
                        "order_id": offer.order_id,
                        "executor_id": offer.executor_id})
    elif request.method == 'PUT':
        offer = update_offer(request.json, uid)
        return jsonify(offer)
    elif request.method == 'DELETE':
        some_delete(Offer, uid)
        return('OK')



if __name__ == "__main__":
    app.run(debug=True)
