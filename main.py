import csv_class as cs
import json_csv_class as cjs
import json_class as js


if __name__ == '__main__':
    JSON_URL = 'https://demo4417994.mockable.io/clientes/'
    CSV_URL = 'https://drive.google.com/file/d/1GlYrv7ex0ClxQwQ0NvJ4GTUGre7s8vtw/view?usp=sharing'
    DIR_DEST_CSV = '/home/denilson/STAGE_MERCOS.csv'

    LISTA_DADOS_JSON = js.treat_json(js.get_online_json(JSON_URL))

    LISTA_DADOS_CSV = cs.data_treatment(cs.import_csv(cs.treat_url_google_drive_file(CSV_URL)))

    LISTA_DADOS_STAGE = cjs.gera_csv_stage(LISTA_DADOS_JSON, LISTA_DADOS_CSV)

    sucesso = cs.write_csv(LISTA_DADOS_STAGE, DIR_DEST_CSV)

    if sucesso:
        print('Sucesso na geração do arquivo csv de STAGE')
    else:
        print('Falha ao criar arquivo csv STAGE')
