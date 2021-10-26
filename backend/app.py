from data_model import *

from typing import Tuple, Union
from flask import Flask, request, Response
import psycopg2
from psycopg2 import sql

db_config = {
    'dbname': 'shop_db', 
    'user': 'docker',
    'password': 'docker',
    'host': 'localhost'
}

app = Flask(__name__)


def insert(table, entry: Model):
    row = entry.content()
    field_names = ', '.join([k for k in row.keys()])
    dummy = ', '.join('%s' for _ in row.keys())
    query = 'INSERT INTO {}({}) VALUES ({})'.format(table, field_names, dummy)
    with psycopg2.connect(**db_config) as conn:
        try:
            with conn.cursor() as cursor:
                    cursor.execute(query, list(row.values())) 
            conn.commit()
        except Exception as e:
            conn.rollback()
            app.logger.info(e)
            return False
    return True



def update_entry(table, entry: Model):
    id = entry.id
    row = entry.content()
    
    fields = ', '.join([f"{k} = %s" for k in row.keys()])
    query = 'UPDATE {} SET {} WHERE id=%s'.format(table, fields)
    
    with psycopg2.connect(**db_config) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (*tuple(row.values()), id))
            return bool(cursor.rowcount)


def delete_by_id(table: str, id: int):
    with psycopg2.connect(**db_config) as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql.SQL("DELETE FROM {} WHERE id=%s".format(table)),[id])


def get_by_id(table: str, id: int) -> Union[Tuple, None]:
    with psycopg2.connect(**db_config) as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql.SQL("SELECT * FROM {} WHERE id=%s".format(table)),[id])
            entry = cursor.fetchone()
            return entry


def get_n(table, limit='ALL', offset=0) -> Tuple:
    query = 'SELECT * FROM {} LIMIT {} OFFSET {}'.format(table, limit, offset)
    with psycopg2.connect(**db_config) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            entries = cursor.fetchall()
            return entries



@app.route('/users', methods=['POST'])
def create_user():
    insert('users', User(**request.get_json()))
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 


@app.route('/users/<int:id>/delete', methods=['POST'])
def delete_user_by_id(id):
    delete_by_id('users', id)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 


@app.route('/users/<int:id>', methods=['POST'])
def update_user_by_id(id):
    entry = User(id=id, **json.loads(request.get_json()))
    update_entry('users', entry=entry)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 


@app.route('/users/<int:id>', methods=['GET'])
def get_user_by_id(id):
    return User(*get_by_id('users', id)).to_json()


@app.route('/users', methods=['GET'])
def get_users(): 
    limit = request.args.get('limit', default='ALL', type=str)
    offset = request.args.get('offset', default=0, type=int)
    users = get_n('users', limit=limit, offset=offset)
    return Response(json.dumps([User(*fields).__dict__ for fields in users]), mimetype='application/json')

@app.route('/orders', methods=['POST'])
def create_order():
    insert('orders', User(**request.get_json()))
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 


@app.route('/orders/<int:id>/delete', methods=['POST'])
def delete_order_by_id(id):
    delete_by_id('orders', id)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 


@app.route('/orders/<int:id>', methods=['POST'])
def update_order_by_id(id):
    entry = User(id=id, **json.loads(request.get_json()))
    update_entry('orders', entry=entry)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 


@app.route('/orders/<int:id>', methods=['GET'])
def get_order_by_id(id):
    return User(*get_by_id('orders', id)).to_json()


@app.route('/orders', methods=['GET'])
def get_orders(): 
    limit = request.args.get('limit', default='ALL', type=str)
    offset = request.args.get('offset', default=0, type=int)
    orders = get_n('orders', limit=limit, offset=offset)
    return Response(json.dumps([Order(*fields).__dict__ for fields in orders]), mimetype='application/json')

@app.route('/deliveries', methods=['POST'])
def create_delivery():
    insert('delivery', User(**request.get_json()))
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 


@app.route('/deliveries/<int:id>/delete', methods=['POST'])
def delete_delivery_by_id(id):
    delete_by_id('delivery', id)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 


@app.route('/deliveries/<int:id>', methods=['POST'])
def update_delivery_by_id(id):
    entry = User(id=id, **json.loads(request.get_json()))
    update_entry('delivery', entry=entry)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 


@app.route('/deliveries/<int:id>', methods=['GET'])
def get_delivery_by_id(id):
    return User(*get_by_id('delivery', id)).to_json()


@app.route('/deliveries', methods=['GET'])
def get_deliveries(): 
    limit = request.args.get('limit', default='ALL', type=str)
    offset = request.args.get('offset', default=0, type=int)
    deliveries = get_n('delivery', limit=limit, offset=offset)
    return Response(json.dumps([Delivery(*fields).__dict__ for fields in deliveries]), mimetype='application/json')

@app.route('/products', methods=['POST'])
def create_product():
    insert('product', User(**request.get_json()))
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 


@app.route('/products/<int:id>/delete', methods=['POST'])
def delete_product_by_id(id):
    delete_by_id('product', id)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 


@app.route('/products/<int:id>', methods=['POST'])
def update_product_by_id(id):
    entry = User(id=id, **json.loads(request.get_json()))
    update_entry('product', entry=entry)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 


@app.route('/products/<int:id>', methods=['GET'])
def get_product_by_id(id):
    return User(*get_by_id('product', id)).to_json()


@app.route('/products', methods=['GET'])
def get_products(): 
    limit = request.args.get('limit', default='ALL', type=str)
    offset = request.args.get('offset', default=0, type=int)
    products = get_n('product', limit=limit, offset=offset)
    return Response(json.dumps([Product(*fields).__dict__ for fields in products]), mimetype='application/json')



@app.route('/restaurants', methods=['POST'])
def create_restaurant():
    insert('restaurant', User(**request.get_json()))
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 


@app.route('/restaurants/<int:id>/delete', methods=['POST'])
def delete_restaurant_by_id(id):
    delete_by_id('restaurant', id)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 


@app.route('/restaurants/<int:id>', methods=['POST'])
def update_restaurant_by_id(id):
    entry = User(id=id, **json.loads(request.get_json()))
    update_entry('restaurant', entry=entry)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 


@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant_by_id(id):
    return User(*get_by_id('restaurant', id)).to_json()


@app.route('/restaurants', methods=['GET'])
def get_restaurants(): 
    limit = request.args.get('limit', default='ALL', type=str)
    offset = request.args.get('offset', default=0, type=int)
    restaurants = get_n('restaurant', limit=limit, offset=offset)
    return Response(json.dumps([Restaurant(*fields).__dict__ for fields in restaurants]), mimetype='application/json')
