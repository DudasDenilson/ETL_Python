import requests
import json


def treat_json(data):
    """
    Função responsável por receber um response json e retornar uma lista de dicionarios.
    """
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

    except Exception as e:
        print(e)
        return list_data_treat


def get_online_json(url):
    """
    Função efetua a obtenção do arquivo json por meio de request. Recebe como parametro de entrada uma Url e retorna um
    request json
    """
    response_json = None
    try:
        request = requests.get(url, timeout=15)
        response_json = request.json()
    except Exception as e:
        print("Falha no request ao arquivo json" + e)

    return response_json


# Funcao criada para usar json local
def get_local_json(caminho):
    """
    Função efetua a obtenção do arquivo json que se encontram locais. Recebe como parametro o local do arquivo e retorna
    um json
    """
    data = None
    try:
        treat_data = {}
        list_data_treat = []
        with open(caminho, "r") as read_file:
            data = json.load(read_file)

    except Exception as e:
        print('Falha ao abrir json local' + e)

    return data
