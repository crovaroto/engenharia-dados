from datetime import timedelta, datetime

#d = datetime.datetime(2024, 1, 20, 19, 45)
#print(d)

#adicionar uma semana
#d = d + datetime.timedelta(weeks = 1)
#print(d)

tipo_carro = 'M'# P, M, G
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()


if tipo_carro == 'P':
  data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
  print(f"O carro chegou às {data_atual} e estará pronto às {data_estimada}") 
elif tipo_carro == 'M':
  data_estimada = data_atual + timedelta(minutes=tempo_medio)
  print(f"O carro chegou às {data_atual} e estará pronto às {data_estimada}")
else:
  data_estimada = data_atual + timedelta(minutes=tempo_grande)
  print(f"O carro chegou às {data_atual} e estará pronto às {data_estimada}")