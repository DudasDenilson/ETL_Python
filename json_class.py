import requests
import json


def treat_json(data):
    """
    Receive response json and return a list of dictionaries
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
        print('JSON treatment failed ' + str(e))
        return list_data_treat


def get_online_json(url):
    """
    Obtain json file by request. Receive as input parameter an URL and return json request.
    """
    response_json = None
    try:
        request = requests.get(url, timeout=15)
        response_json = request.json()
    except Exception as e:
        print("JSON request failed " + str(e))

    return response_json


def get_local_json(caminho):
    """
    Get Json file from physical machine. Receive the file's location in parameter and return a Json.
    """
    data = None
    try:
        with open(caminho, "r") as read_file:
            data = json.load(read_file)

    except Exception as e:
        print('Failed to open local JSON ' + str(e))

    return data
