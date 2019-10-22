import pandas as pd
from pandas import DataFrame
from datetime import datetime, timedelta


# funcao responsavel pela leitura do arquivo csv
def import_csv(url_local):
    try:
        data = pd.read_csv(url_local, sep=",", encoding='utf-8', quotechar='"', decimal='.')
    except:
        print("Falha na leitura do arquivo csv")

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
        mes = fullplano[len(fullplano) - 1:]

        # Calculo de valor do produto
        valor = line[2].replace(',', '.').replace(' ', '')
        val_convertido = valor[2:].strip()
        val = float(val_convertido) / int(mes)

        # Criação de uma lista com dicionarios de todos os pagamentos

        treat_data = {
            'id_cliente': line[0],
            'data': line[1],
            'valor_total': val_convertido,
            'plano': plano,
            'meses': mes,
            'valor_mes': val
        }
        list_data_treat.append(treat_data)
    return list_data_treat


def write_csv(lista_dict_origem, caminho_csv_destino):
    data = import_csv(lista_dict_origem)
    listadados = data_treatment(data)
    df = DataFrame(listadados, columns=['id_cliente', 'data', 'valor_total', 'plano', 'meses', 'valor_mes'])
    export_csv = df.to_csv(caminho_csv_destino, index=None, header=True)


url = 'https://doc-0c-68-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/g5globpfkhe1iqgu865sj11mn13ec05v/1571623200000/04105005953058485704/*/1GlYrv7ex0ClxQwQ0NvJ4GTUGre7s8vtw?e=download'
local = '/home/denilson/Downloads/pagamentos.csv'
data = import_csv(local)
listadados = data_treatment(data)
print(listadados)
destino = '/home/denilson/export_datafram.csv'
write_csv(local, destino)






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
