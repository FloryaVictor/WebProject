import requests

# a = '["{\n \"id\": 1,\n \"email\": \"pupkin@mail.ru\",\n \"name\": \"vasya\",\n \"password\": \"strong pass\",\n \"phone_number\": \"88005553535\",\n \"role\": \"customer\",\n \"address\": \"\\u0443\\u043b\\u0438\\u0446\\u0430 \\u041f\\u0443\\u0448\\u043d\\u043a\\u0438\\u043d\\u0430, 4\",\n \"balance\": 0.0\n}", "{\n \"id\": 2,\n \"email\": \"sergeich@gmail.com\",\n \"name\": \"sergey\",\n \"password\": \"ochen strong pass\",\n \"phone_number\": \"89231721754\",\n \"role\": \"customer\",\n \"address\": \"\\u041e\\u043c\\u0441\\u043a\",\n \"balance\": 0.0\n}"]'
# print(a)

resp = requests.post('http://localhost:5000/users/3/delete')
print(resp.content)