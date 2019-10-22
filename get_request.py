import requests
import json
import main
from main import import_csv

url = 'https://demo4417994.mockable.io/clientes/'
url1 = '/home/denilson/clientes.json'

with open(url1, "r") as read_file:
    data = json.load(read_file)

response = requests.get(url)


#print(data)

#for r in data:
#    print(r["nome"])

response_json = response.json()
print(response_json)

for v in response_json:
    print(v["cidade"])
