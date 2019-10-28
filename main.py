from google.cloud import bigquery
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('/home/denilson/Documents/Projeto1-4780fa1a64d4.json')
project_id = 'projeto1-256320'
client = bigquery.Client(credentials=credentials, project=project_id)
dataset_id = 'PR'
job_config = bigquery.QueryJobConfig()

table_ref = client.dataset(dataset_id).table('FT_PAGAMENTOS1')
job_config.destination = table_ref


query = 'SELECT *  FROM PR.STAGE_PAGAMENTOS  LIMIT 1'
query_create = """
select f.*,
case when new_mrr = 1 then "NEW_MRR"
when valor_mes > valor_ant_pag then "EXPANSION"
when valor_ant_pag > valor_mes then "CONTRACTION"
when date_trunc( data_pagamento, MONTH) >  date_trunc(date_add(data_ant_pag_fim, interval 1 month), MONTH) then "RESURRECTED"
when data_pagamento = ultimo_pagamento and data_pagamento < date_trunc(current_date, MONTH)  
and proximo_pagamento is null
then "CANCELLED"
else "MRR"
end as metrica,
case 
when new_mrr = 1 then valor_mes
when valor_mes > valor_ant_pag then valor_mes- valor_ant_pag
when valor_ant_pag > valor_mes then valor_ant_pag -valor_mes
when date_trunc( data_pagamento, MONTH) > date_trunc(date_add(data_ant_pag_fim, interval 1 month), MONTH) then valor_mes
when data_pagamento = ultimo_pagamento and date_trunc(data_pagamento_fim,month) < date_trunc(current_date,month)
and proximo_pagamento is null
then valor_mes
else valor_mes
end as valor_metrica,
case
when data_pagamento = ultimo_pagamento and date_trunc(data_pagamento_fim,month) < date_trunc(current_date,month) 
and proximo_pagamento is null
and data_ant_pag_fim is not null then 0
else valor_mes 
end valor_mrr
from (SELECT 
id_cliente,
data_pagamento,
valor_total,
plano,
empresa_nome,
cidade,
estado,
segmento,
data_pagamento_fim,
date_trunc( data_pagamento, MONTH) mes_ano_pagamento,
count(id_cliente) over (partition by id_cliente) new_mrr,
lag(valor_mes) over (partition by id_cliente order by id_cliente, data_pagamento) valor_ant_pag,
valor_mes,
lead(valor_mes) over (partition by id_cliente order by id_cliente, data_pagamento) valor_pos_pag,
lag(data_pagamento) over (partition by id_cliente order by id_cliente, data_pagamento) data_ant_pag_fim,
last_value(data_pagamento) over (partition by id_cliente order by id_cliente ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) ultimo_pagamento,
lead(data_pagamento) over (partition by id_cliente order by id_cliente, data_pagamento) proximo_pagamento
FROM `projeto1-256320.PR.STAGE_PAGAMENTOS`
order by id_cliente, data_pagamento)f;
"""

#query_job = client.query(query_create, project=project_id)

query_job = client.query(
    query_create,
    # Location must match that of the dataset(s) referenced in the query
    # and of the destination table.
    job_config=job_config)


results = query_job.result()

print(results)
print('Query results loaded to table {}'.format(table_ref.path))


