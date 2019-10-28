import requests
import json


def treat_json(data):
    list_data_treat = []

    try:
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

    except:
        return list_data_treat


def get_online_json(url):
    response_json = None
    try:
        request = requests.get(url, timeout=15)
        response_json = request.json()
    except:
        print("Falha no request ao arquivo json")

    return response_json


# Funcao criada para usar json local
def get_local_json(caminho):
    data = None
    try:
        treat_data = {}
        list_data_treat = []
        with open(caminho, "r") as read_file:
            data = json.load(read_file)

    except:
        print('Falha ao abrir json local')

    return data
