from datetime import datetime
import pandas as pd
from dateutil.relativedelta import relativedelta
from pandas import DataFrame


def import_csv(local):
    """
    Perform CSV import , receive at parameter a location where the file is, can be a physical
    machine location or a URL and return a panda dataframe.
    """

    data = None
    try:
        print('Starting CSV import')
        data = pd.read_csv(local, sep=",")
        print('CSV import is done')
    except Exception as e:
        print('Problem to open CSV ' + str(e))

    return data


def data_treatment(csv_data):
    """
    Perform data processing on received dataframe. Receive a dataframe and return a list of dictionaries.
    """
    print('Starting treating CSV data')
    list_data_treat = []
    try:

        for line in csv_data.values:
            # Treat plan name
            fullplano = line[3]
            plano = fullplano[:len(fullplano) - 2]

            # Find how many month has payment
            mes = int(fullplano[len(fullplano) - 1:])

            # Calculate product price
            valor = line[2].replace(',', '.').replace(' ', '')
            val_convertido = valor[2:].strip()
            val = float(val_convertido) / mes

            # Calculate final date payment
            date_str = line[1]
            data_final = datetime.strptime(date_str, '%d/%m/%Y').date()
            data_padrao = datetime.strptime(date_str, '%d/%m/%Y').date()
            data_padrao = (data_padrao + relativedelta(months=mes - 1))

            # Create a dictionary list with all payments
            if mes > 1:
                for m in range(mes):
                    data_calculada = (data_final + relativedelta(months=int(m)))

                    treat_data = {
                        'id_cliente': line[0],
                        'data': data_calculada,
                        'valor_total': val_convertido,
                        'plano': plano,
                        'meses': 1,
                        'valor_mes': val,
                        'data_final_pag': data_padrao
                    }
                    list_data_treat.append(treat_data)
            else:

                treat_data = {
                    'id_cliente': line[0],
                    'data': data_final,
                    'valor_total': val_convertido,
                    'plano': plano,
                    'meses': mes,
                    'valor_mes': val,
                    'data_final_pag': data_padrao
                }

                list_data_treat.append(treat_data)
    except Exception as e:
        print('CSV treat failed' + str(e))

    print('CSV treatments done')
    return list_data_treat


def write_csv(lista_dict_origem, caminho_csv_destino):
    """
    Perform CSV write using a dictionary list receive at parameter on specific local.
    """
    sucess = False
    try:
        print('Starting CSV write')
        # Get keys at parameter list
        colunas = lista_dict_origem[0].keys()
        array_colunas = []

        # Create array with all columns
        for r in colunas:
            array_colunas.append(r)

        # Create dataframe based on columns above
        df = DataFrame(lista_dict_origem, columns=array_colunas)

        # Sort CSV data using columns 0 and 1
        df = df.sort_values(by=[array_colunas[0], array_colunas[1]])

        # Create CSV
        df.to_csv(caminho_csv_destino, index=None, header=True)
        sucess = True

        print('CSV write process is done')
    except Exception as e:
        print('Failed to write CSV ' + str(e))

    return sucess


def treat_url_google_drive_file(url):
    """
    Performs treatment at Google drive URL's, so that access to the file is possible. Receive a URL e transform to
    another URL to download file.
    """
    dwn_url = None
    try:
        file_id = url.split('/')[-2]
        if len(file_id) < 2:
            dwn_url = None
        else:
            dwn_url = 'https://drive.google.com/uc?export=download&id=' + file_id
    except Exception as e:
        print('URL treatment failed : ' + str(e))

    return dwn_url
