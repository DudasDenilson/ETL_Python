from datetime import date, datetime
from dateutil.relativedelta import relativedelta

date_time_str = '02-01-2019'
data = datetime.strptime(date_time_str, '%d-%m-%Y')

six_months = data.date() + relativedelta(months=+6)

print(six_months)