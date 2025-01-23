import datetime
import pytz

d = datetime.datetime.now(pytz.timezone('America/Sao_Paulo'))
print(d)

#Outra forma
d = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=3), "BRT"))
print(d)

d_utc = d.astimezone(datetime.timezone.utc)
print(d_utc)