from datetime import datetime
import pandas as pd
from dateutil.relativedelta import relativedelta
from pandas import DataFrame


def import_csv(local):
    """
    Função responsavel pela importação do arquivo csv, recebendo como parametro local onde o arquivo se encontra,
    podendo este ser uma URl ou local na maquina fisica, tendo como retorno um panda dataframe
    """

    data = None
    try:
        print('Inicializando Importação csv')
        data = pd.read_csv(local, sep=",")
        print('Finalizado Importação csv')
    except Exception as e:
        print('Falha ao abrir arquivo csv ' + e)

    return data


# funcao responsavel pelo tratamentos dos dados do arquivo csv
def data_treatment(csv_data):
    """
    Função criada para efetuar o tratamento de dados do arquivo dataframe recebido. Possui como parametro de entrada o
    dataframe e como retorno uma lista de dicionarios.
    """
    print('Iniciando tratamento de dados CSV')
    list_data_treat = []
    try:

        for line in csv_data.values:
            # Responsavel pelo tratamento do nome do plano
            fullplano = line[3]
            plano = fullplano[:len(fullplano) - 2]

            # Busca os dados de quantos meses foram pagos
            mes = int(fullplano[len(fullplano) - 1:])

            # Calculo de valor do produto
            valor = line[2].replace(',', '.').replace(' ', '')
            val_convertido = valor[2:].strip()
            val = float(val_convertido) / mes

            # Calculo de data mes final do pagamento
            date_str = line[1]
            data_final = datetime.strptime(date_str, '%d/%m/%Y').date()
            data_padrao = datetime.strptime(date_str, '%d/%m/%Y').date()
            data_padrao = (data_padrao + relativedelta(months=mes - 1))

            # Criação de uma lista com dicionarios de todos os pagamentos
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
        print('Falha ao tratar csv' + e)

    print('Finalizado tratamento CSV')
    return list_data_treat


def write_csv(lista_dict_origem, caminho_csv_destino):
    """
    Função responsavel por escrever a lista de dicionarios recebidos em arquivo csv, recebendo como dados a lista de dicionario e o caminho
    onde sera escrito os csv.
    """
    sucess = False
    try:
        print('Iniciado gravação do CSV')
        # Obtem as keys da lista passada por parametro
        colunas = lista_dict_origem[0].keys()
        array_colunas = []
        # Cria um array com todas as colunas
        for r in colunas:
            array_colunas.append(r)
        # Efetua a criação do dataframe com base nas colunas obtidas
        df = DataFrame(lista_dict_origem, columns=array_colunas)
        # Classifica os dados do CSV nas colunas 0 e 1
        df = df.sort_values(by=[array_colunas[0], array_colunas[1]])
        # Cria o CSV
        export_csv = df.to_csv(caminho_csv_destino, index=None, header=True)
        sucess = True
        print('Processo de escrita finalizado')
    except Exception as e:
        print('Falha gravacao CSV' + e)

    return sucess


def treat_url_google_drive_file(url):
    """
    Função responsável pelo tratamentos de urls do google drive, para que seja possivel o acesso ao arquivo. Recebe a
    url compartilhada do arquivo e transforma em Url de Download.
    """
    dwn_url = None
    try:
        file_id = url.split('/')[-2]
        dwn_url = 'https://drive.google.com/uc?export=download&id=' + file_id
    except Exception as e:
        print('Falha ao tratar URL' + e)

    return dwn_url
