from pandas import DataFrame
import csv_class

def write_csv(caminho_csv_origem, caminho_csv_destino):
    data = csv_class.import_csv(caminho_csv_origem)
    listadados = csv_class.data_treatment(data)
    df = DataFrame(listadados, columns=['id_cliente', 'data', 'valor_total', 'plano', 'meses', 'valor_mes'])
    export_csv = df.to_csv(caminho_csv_destino, index=None, header=True)



local = '/home/denilson/Downloads/pagamentos.csv'
destino = '/home/denilson/export_datafram.csv'


write_csv(local, destino)

