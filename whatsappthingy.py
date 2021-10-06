import datetime 
date = datetime.datetime.fromordinal(730920)

nexttime = date.today()

while True:
    nexttime = nexttime + datetime.timedelta(minutes=3)
    print(nexttime.hour, nexttime.minute)
