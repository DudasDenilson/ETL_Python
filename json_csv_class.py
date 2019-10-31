def gera_csv_stage(lista_dados_json, lista_dados_csv):
    """
    Function responsible for joining the data received through csv and json, generating a list of
    dictionaries. It receives as parameters a list of json dictionaries and a list of csv dictionaries, having as
    I return a new list of dictionaries.
    """
    # Create a list to store the processed data.
    print('Starting Stage treatment')
    list_data_treat = []
    try:
        # Browse csv list
        for r_csv in lista_dados_csv:
            # Browse json list
            for r_json in lista_dados_json:
                # Join list using id
                if r_csv.get("id_cliente") == r_json.get("id"):
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
    except Exception as e:
        print('Treatment Stage failed ' + str(e))

    return list_data_treat
