import json

from flask import request

from models import User, Order, Offer
from main import db


def load_users_json(data):
        for row in data:
            user_db = User(id=row.get('id'),
                        first_name=row.get('first_name'),
                        last_name=row.get('last_name'),
                        age=row.get('age'),
                        email=row.get('email'),
                        role=row.get('role'),
                        phone=row.get('phone')
                   )
            db.session.add(user_db)
        db.session.commit()

def load_orders_json(data):
        for row in data:
            db.session.add(Order(id=row.get('id'),
                                name=row.get('name'),
                                description=row.get('description'),
                                start_date=row.get('start_date'),
                                end_date=row.get('end_date'),
                                address=row.get('address'),
                                price=row.get('price'),
                                customer_id=row.get('customer_id'),
                                executor_id=row.get('executor_id'))
                           )
        db.session.commit()

def load_offers_json(data):
        for row in data:
            db.session.add(Offer(id=row.get('id'),
                                order_id=row.get('order_id'),
                                executor_id=row.get('executor_id'))
                           )
        db.session.commit()

db.drop_all()
db.create_all()

with open('bd/users.json', 'r', encoding="UTF-8") as file:
    load_users_json(json.load(file))

with open('bd/orders.json', 'r', encoding="UTF-8") as file:
    load_orders_json(json.load(file))

with open('bd/offers.json', 'r', encoding="UTF-8") as file:
    load_offers_json(json.load(file))

def update_offer(data, uid):
    offer = Offer.query.get(uid)
    offer.id = data.get('id')
    offer.order_id = data.get('order_id')
    offer.executor_id = data.get('executor_id')
    db.session.add(offer)
    db.session.commit()
    return offer

def update_order(data, uid):
    order = Order.query.get(uid)
    order.id = data.get('id')
    order.name = data.get('name')
    order.description = data.get('description')
    order.start_date = data.get('start_date')
    order.end_date = data.get('end_date')
    order.address = data.get('address')
    order.price = data.get('price')
    order.customer_id = data.get('customer_id')
    order.executor_id = data.get('executor_id')
    db.session.add(order)
    db.session.commit()
    return order

def update_user(data, uid):
    user = User.query.get(uid)
    user.id = data.get('id')
    user.first_name = data.get('first_name')
    user.last_name = data.get('last_name')
    user.age = data.get('age')
    user.email = data.get('email')
    user.role = data.get('role')
    user.phone = data.get('phone')
    db.session.add(user)
    db.session.commit()
    return user

def some_delete(model, uid):
    some = model.query.get(uid)
    db.session.delete(some)
    db.session.commit()
