import csv_class
import json_class















local = '/home/denilson/Downloads/pagamentos.csv'
# url_csv = 'https://doc-08-3o-docs.googleusercontent.com/docs/securesc/itgof2bk0rq38g93e3k3bbkt36b80r5j/bukdvqqreor3faj6mco62fgk5cbu3mcn/1571716800000/04105005953058485704/02359347683867043271/1GlYrv7ex0ClxQwQ0NvJ4GTUGre7s8vtw?e=download'
datas = csv_class.csv_etl.import_csv(local)
listadados = csv_class.csv_etl.data_treatment(datas)

# url1 = '/home/denilson/clientes.json'
# listajson = json_class.get_local_json(url1)

url = 'https://demo4417994.mockable.io/clientes/'
listajson = json_class.json_etl.get_online_json(url)
list_data_treat = []
for r_csv in listadados:
    for r_json in listajson:
        if r_csv["id_cliente"] == r_json["id"]:
            treat_data = {}
            # if r_csv.get("id_cliente") == 1030:
            # print(f' atual : {r_csv.get("valor_mes")} -> next : {r_csv.get("valor_mes").__next__()}')
            #    print(r_csv.__getitem__("valor_mes"))
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

destinocsv = '/home/denilson/export.csv'
csv_class.csv_etl.write_csv(list_data_treat, destinocsv)
