from pandas import DataFrame
import csv_class

local = '/home/denilson/Downloads/pagamentos.csv'
data = csv_class.import_csv(local)
listadados = csv_class.data_treatment(data)

df = DataFrame(listadados, columns=['id_cliente', 'data', 'valor_total', 'plano', 'meses', 'valor_mes'])

export_csv = df.to_csv(r'/home/denilson/export_dataframe.csv', index=None,
                       header=True)  # Don't forget to add '.csv' at the end of the path

print(df)
