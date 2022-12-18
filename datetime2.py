#get today's datewind
from datetime import date
today=date.today()
print("today's date",today)

d1=today.strftime("%d %m %Y")
print("d1=",d1)


d2=today.strftime("%B %d,%Y")
print("d2=",d2)

## get current date and time
from datetime import datetime
now=datetime.now()
print("now=",now)
