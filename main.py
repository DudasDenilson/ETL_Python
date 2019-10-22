from google.cloud import bigquery
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('/home/denilson/Documents/Projeto1-4780fa1a64d4.json')
project_id = 'projeto1-256320'
client = bigquery.Client(credentials=credentials, project=project_id)

print(client)

query_job = client.query("""
  SELECT *
  FROM PR.PAGAMENTOS
  LIMIT 1""")
results = query_job.result()

for row in results:
    print("{} : {} ".format(row.ID_CLIENTE, row.PLANO))


