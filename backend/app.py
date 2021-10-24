from data_model import *

from typing import Tuple, Union
from flask import Flask
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
    row = entry.get_no_id(('id', ))
    
    field_names = ', '.join([k for k, v in row.items() if v is not None])
    field_values = list(filter(lambda v: v is not None, row.values()))
    dummy = ', '.join('%s' for _ in field_values)
   
    query = 'INSERT INTO {}({}) VALUES ({})'.format(table, field_names, dummy)
    print(query)
    with psycopg2.connect(**db_config) as conn:
        with conn.cursor() as cursor:
                cursor.execute(query, field_values) 
        conn.commit()


def update_entry(table, entry: Model):
    row = entry.get_no_id(('id', ))
    id = entry.id
    
    fields = ', '.join([f"{k} = %s" for k in row.keys()])
    query = 'UPDATE {} SET {} WHERE id=%s'.format(table, fields)

    with psycopg2.connect(**db_config) as conn:
        with conn.cursor() as cursor:
                cursor.execute(query, (*row.values(), id)) 


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



@app.route('/')
def hello_world():
    return 'Hello, friend!'


