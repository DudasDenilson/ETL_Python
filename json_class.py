import requests
import json


def get_online_json(url):
    treat_data = {}
    list_data_treat = []
    try:
        response = requests.get(url)
        response_json = response.json()
    except:
        print("Falha no request ao arquivo json")

    for line in response_json:
        treat_data = {
            'id': line["id"],
            'nome': line["nome"],
            'cidade': line["cidade"],
            'estado': line["estado"],
            'segmento': line["segmento"],
        }
        list_data_treat.append(treat_data)
    return list_data_treat


def get_local_json(caminho):
    treat_data = {}
    list_data_treat = []
    with open(caminho, "r") as read_file:
        data = json.load(read_file)

    for line in data:
        treat_data = {
            'id': line["id"],
            'nome': line["nome"],
            'cidade': line["cidade"],
            'estado': line["estado"],
            'segmento': line["segmento"],
        }
        list_data_treat.append(treat_data)
    return list_data_treat


url = 'https://demo4417994.mockable.io/clientes/'

url1 = '/home/denilson/clientes.json'

#print(get_local_json(url1))
print(get_online_json(url))
