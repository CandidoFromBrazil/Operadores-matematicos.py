#Contador de horas, consulta médica;

#1m = 60s
#1h = 60m
#E uma 1h em segundos? = 1h = 60m * 60s = 3600s
#1d = 24h = 86400s

segundos = int(input('entre com os segundos: ')) # Começar com 86400s
minutos = segundos // 60 #conversão de segundos para minutos
horas = minutos // 60 # conversão de minutos para hora
dias = horas // 24 # conversão de horas para dias

recsegundo = (dias + horas + minutos + segundos)

print(f'Há: {dias}d, {horas}h:{minutos}m:{segundos}s. Desde a sua ultima consulta')
print(f'Em segundo isso seria: {recsegundo}s')







