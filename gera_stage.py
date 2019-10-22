import csv_class
import json_class

local = '/home/denilson/Downloads/pagamento.csv'
#url_csv = 'https://doc-08-3o-docs.googleusercontent.com/docs/securesc/itgof2bk0rq38g93e3k3bbkt36b80r5j/bukdvqqreor3faj6mco62fgk5cbu3mcn/1571716800000/04105005953058485704/02359347683867043271/1GlYrv7ex0ClxQwQ0NvJ4GTUGre7s8vtw?e=download'
datas = csv_class.import_csv(local)
listadados = csv_class.data_treatment(datas)

#url1 = '/home/denilson/clientes.json'
#listajson = json_class.get_local_json(url1)

url = 'https://demo4417994.mockable.io/clientes/'
listajson = json_class.get_online_json(url)
list_data_treat = []
for r_csv in listadados:
    for r_json in listajson:
        if r_csv["id_cliente"] == r_json["id"]:
            treat_data = {}

            treat_data = {
                'id_cliente': r_csv["id_cliente"],
                'data_pagamento': r_csv["data"],
                'valor_total': r_csv["valor_total"],
                'plano': r_csv["plano"],
                'meses': r_csv["meses"],
                'valor_mes': r_csv["valor_mes"],
                'empresa_nome' : r_json["nome"],
                'cidade':r_json["cidade"],
                'estado':r_json["estado"],
                'segmento':r_json["segmento"],
                'data_pagamento_fim': r_csv["data_final_pag"]
            }
            list_data_treat.append(treat_data)



destinocsv = '/home/denilson/export.csv'
csv_class.write_csv(list_data_treat,destinocsv)