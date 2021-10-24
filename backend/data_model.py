import json

from copy import copy

class Model:
    def __init__(self):
        pass
    
    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, dump):
        return cls(**json.loads(dump))

    def __str__(self) -> str:
        return self.to_json()

    def get_no_id(self, id_names: tuple = None) -> dict:
        cp = copy(self.__dict__)
        for name in id_names:
            del cp[name]
        return cp


class User(Model):
    def __init__(self, id=None, email=None, name=None, password=None, phone_number=None, role=None, address=None, balance=None):
            super().__init__()
            self.id = id
            self.email = email
            self.name = name
            self.password = password
            self.phone_number = phone_number
            self.role = role
            self.address = address
            self.balance = balance

class Product(Model):
    def __init__(self, id=None, name=None, description=None, price=None, photo_url=None):
        super().__init__()
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.photo_url = photo_url

class Order(Model):
    def __init__(self, id=None, price=None, date=None, customer_id=None, restautrant_id=None, delivery_id=None):
        super().__init__()
        self.id = id
        self.price = price
        self.date = date
        self.customer_id = customer_id
        self.restautrant_id = restautrant_id
        self.delivery_id = delivery_id

class Delivery(Model):
    def __init__(self, id=None, name=None, price=None, rating=None):
        super().__init__()
        self.id = id
        self.name = name
        self.price = price
        self.rating = rating
    
class Restaurant(Model):
    def __init__(self, id=None, name=None, address=None, rating=None, description=None):
        super().__init__()
        self.id = id
        self.name = name
        self.address = address
        self.rating = rating 
        self.description = description
