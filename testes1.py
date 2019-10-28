import pandas as pd
from io import StringIO
import requests
from csv_class import *
import tests_data

#url = 'https://demo4417994.mockable.io/clientes/'
csv = ' https://drive.google.com/uc?export=download&id=1GlYrv7ex0ClxQwQ0NvJ4GTUGre7s8vtw'


result = data_treatment(import_csv(tests_data.LOCAL_VALID_PART_CSV))
for val in result:
    count = 0
    for k in val.keys():
        print(k)
        assert 'id_cliente' in k
        count +=1
        if count == 1:
           break
    break


#orig_url='https://drive.google.com/file/d/1GlYrv7ex0ClxQwQ0NvJ4GTUGre7s8vtw/view?usp=sharing'

#file_id = orig_url.split('/')[-2]
#dwn_url='https://drive.google.com/uc?export=download&id=' + file_id
#url = requests.get(dwn_url).text
#csv_raw = StringIO(url)
#dfs = pd.read_csv(dwn_url)
#print(dfs.head())