import csv_class
import json_class


def gera_csv_stage(lista_dados_json, lista_dados_csv):
    # Cria uma lista para armazenar os dados processados
    print('Iniciado tratamento stage')
    list_data_treat = []
    try:
        # Percorre a lista do csv
        for r_csv in lista_dados_csv:
            # Percorre a lista do json
            for r_json in lista_dados_json:
                # Efetua o join entre as duas listas
                if r_csv["id_cliente"] == r_json["id"]:
                    treat_data = {
                        'id_cliente': r_csv.get("id_cliente"),
                        'data_pagamento': r_csv.get("data"),
                        'valor_total': r_csv.get("valor_total"),
                        'plano': r_csv.get("plano"),
                        'meses': r_csv.get("meses"),
                        'valor_mes': r_csv.get("valor_mes"),
                        'empresa_nome': r_json.get("nome"),
                        'cidade': r_json.get("cidade"),
                        'estado': r_json.get("estado"),
                        'segmento': r_json.get("segmento"),
                        'data_pagamento_fim': r_csv.get("data_final_pag")
                    }
                    list_data_treat.append(treat_data)
    except:
        print('Falha no tratamento da stage')

    return list_data_treat
