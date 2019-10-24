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
