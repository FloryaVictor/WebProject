import requests
import json
url = 'order'

data = {
    "price": "15", 
    "date": "05.10.2021", 
    "customer_id": "2", 
    "restaurant_id": "1", 
    "delivery_id": "1"
}
resp = requests.post(f'http://localhost:5000/{url}', json=json.dumps(data))
print(resp.content)