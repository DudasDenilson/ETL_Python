import pandas as pd
from pandas import DataFrame
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta, date


# funcao responsavel pela leitura do arquivo csv
def import_csv(url_local):
    data = pd.read_csv(url_local, sep=",")
    return data


# funcao responsavel pelo tratamentos dos dados do arquivo csv
def data_treatment(csv_data):
    treat_data = {}
    list_data_treat = []

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
        data_padrao = (data_padrao + relativedelta(months=mes-1))

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

    print('Finalizado data_treat')
    return list_data_treat


def write_csv(lista_dict_origem, caminho_csv_destino):
    colunas = lista_dict_origem[0].keys()
    array_colunas=[]
    for r in colunas:
        array_colunas.append(r)
    df = DataFrame(lista_dict_origem, columns=array_colunas)
    df = df.sort_values(by=[array_colunas[0], array_colunas[1]])
    export_csv = df.to_csv(caminho_csv_destino, index=None, header=True)


#url = 'https://doc-08-3o-docs.googleusercontent.com/docs/securesc/itgof2bk0rq38g93e3k3bbkt36b80r5j/bidrdkamhm6200497ij5l9kaj7ft727s/1571745600000/04105005953058485704/02359347683867043271/1GlYrv7ex0ClxQwQ0NvJ4GTUGre7s8vtw?e=download&nonce=vba8gnpevikbi&user=02359347683867043271&hash=qmpgj9rs4ofuunf0d332dn673f69dfck'
#local = '/home/denilson/Downloads/pagamento.csv'
#data = import_csv(local)
#listadados = data_treatment(data)
#print(listadados)
#destino = '/home/denilson/export_datafram.csv'
#write_csv(listadados, destino)






# for k in data.values:
#    fullplano = k[3]
#    plano = fullplano[:len(fullplano) - 2]
#    mes = fullplano[len(fullplano) - 1:]

#    mes_calc = datetime.strptime(k[1], '%d/%m/%Y')
#    dias = int(mes) * 30

#    mes_calc = mes_calc + timedelta(days=dias)
#    print(mes_calc)

#    print(
#        f'O ID_CLIENTE {k[0]} comprou o plano {plano} em {k[1]} e pagou o valor de {k[2]} e esta valido por {mes} ate {mes_calc}')
