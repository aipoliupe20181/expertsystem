from pandas import pandas as pd
from datetime import date, datetime
import csv

### READ FILE.CSV
dataset = pd.read_csv('servidores2.csv',usecols=['hash_cpf','data_cargo','carga_horaria_semanal','valor_bruto_mensal_para_o_mes_de_ref'])

### DEFINE TOTAL ROWS
total = int(dataset.hash_cpf.count())
var1 = dataset.data_cargo.str.split('-')

### WRITE NEW DATA
with open('servidorestable.csv', 'w', newline='') as csvfile:
	fieldnames = ['hash_cpf','tempo_cargo','valor_bruto_mensal_para_o_mes_de_ref']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	for row in range(0,total):
		var2 = 2017 - int(var1[row][2])
		writer.writerow({'hash_cpf': dataset.hash_cpf[row], 'tempo_cargo': var2, 'valor_bruto_mensal_para_o_mes_de_ref': dataset.valor_bruto_mensal_para_o_mes_de_ref[row]})
