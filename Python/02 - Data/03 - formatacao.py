import datetime

d = datetime.datetime.now()
print(d)
print(d.strftime("%d/%m/%Y %H:%M"))

date_string = "21/01/2025 19:14"
d = datetime.datetime.strptime(date_string, "%d/%m/%Y %H:%M")
print(d)