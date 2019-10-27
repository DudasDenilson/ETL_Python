import json_class
import csv_class


url = 'https://demo4417994.mockable.io/clientes/'
lista_json = json_class.get_online_json(url)

data = json_class.treat_json(lista_json)
print(data)