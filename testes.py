from datetime import datetime
import datetime as dttime


date_time_str = '02-12-2019'
date_time_obj = dttime.datetime.strptime(date_time_str, '%d-%m-%Y')
dt = date_time_obj


print('Date:', date_time_obj.date())
print('Time:', date_time_obj.time())
print('Date-time:', date_time_obj)
timestampobj = datetime.timestamp(date_time_obj)
meses=5

print('timestamp:', timestampobj)

for x in range(meses):
    print(x)

# current date and time
# now = datetime.now()
# data = '2018-06-29'
# data = dttime.date(data)



##CODIGO PARA TESTES CSV_CLASS

# url = 'https://doc-08-3o-docs.googleusercontent.com/docs/securesc/itgof2bk0rq38g93e3k3bbkt36b80r5j/bidrdkamhm6200497ij5l9kaj7ft727s/1571745600000/04105005953058485704/02359347683867043271/1GlYrv7ex0ClxQwQ0NvJ4GTUGre7s8vtw?e=download&nonce=vba8gnpevikbi&user=02359347683867043271&hash=qmpgj9rs4ofuunf0d332dn673f69dfck'
# local = '/home/denilson/Downloads/pagamento.csv'
# data = import_csv(local)
# listadados = data_treatment(data)
# print(listadados)
# destino = '/home/denilson/export_datafram.csv'
# write_csv(listadados, destino)