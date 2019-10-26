import requests
import json


# Função criada para obter json online
def get_online_json(url):
    global response_json
    treat_data = {}
    list_data_treat = []
    # Efetua a tentiva de request
    try:
        response = requests.get(url)
        response_json = response.json()
    except:
        print("Falha no request ao arquivo json")
        # Da inicio a criação de uma lista com os dados obtidos do json
    for line in response_json:
        treat_data = {
            'id': line["id"],
            'nome': line["nome"],
            'cidade': line["cidade"],
            'estado': line["estado"],
            'segmento': line["segmento"],
        }
        list_data_treat.append(treat_data)
    # Retorna a lista montada
    return list_data_treat


# Funcao criada para usar json local
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
