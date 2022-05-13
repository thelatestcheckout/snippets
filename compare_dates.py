from datetime import date, datetime

timestamp = 1545730073
today = date.today()
dt_object = datetime.fromtimestamp(timestamp).date()

if today == dt_object:
    print("same date")
else:
    print("different date")
