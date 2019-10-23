from google.cloud import bigquery
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('/home/denilson/Documents/Projeto1-4780fa1a64d4.json')
project_id = 'projeto1-256320'
client = bigquery.Client(credentials=credentials, project=project_id)

query = 'SELECT *  FROM PR.STAGE_PAGAMENTOS  LIMIT 1'


query_job = client.query(query, project=project_id)
results = query_job.result()

for row in results:
    print(row)


