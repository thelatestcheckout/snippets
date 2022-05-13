from datetime import datetime
from timeit import timeit

date_time_str = '12.05.22 13:55'

# convert date time string to datetype object
date_time_obj = datetime.strptime(date_time_str, '%d.%m.%y %H:%M')

# convert datetype object to timestamp
time_timestamp = datetime.timestamp(date_time_obj)
print(time_timestamp)

# find current time stamp
current_time = datetime.now(tz=None)
print(datetime.timestamp(current_time))
