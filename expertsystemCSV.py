#!/usr/bin/python
import json
from pandas import pandas as pd
from datetime import date, datetime
import csv

salarioMinimo = 965
valorPoupadoMensal = 0
indicador = 0

### START OF RULES ###
def a():
    if(salario < salarioMinimo):
        global valorPoupadoMensal
        valorPoupadoMensal = 0
        rulesWithValues['a'] += 1


def b():
    if(salario >= salarioMinimo and salario < salarioMinimo*5):
        global valorPoupadoMensal
        valorPoupadoMensal = (5/100)*salario
        rulesWithValues['b'] += 1


def c():
    if(salario >= salarioMinimo*5 and salario < salarioMinimo*10):
        global valorPoupadoMensal
        valorPoupadoMensal = (10/100)*salario
        rulesWithValues['c'] += 1


def d():
    if(salario >= salarioMinimo*10):
        global valorPoupadoMensal
        valorPoupadoMensal = (20/100)*salario
        rulesWithValues['d'] += 1


def e():
    if(valorPoupadoMensal*tempoDeServico < valorImovel):
        rulesWithValues['e'] += 1
        global indicador
        indicador += 1


def f():
    if(valorPoupadoMensal*tempoDeServico >= valorImovel):
        rulesWithValues['f'] += 1
### END OF RULES ###


### START OF DICTIONARYS ###
# Load the rule's priority value from a text file
# The file should be i.e {"a": 2, "b": 1, "c": 0}
rulesWithValues = json.load(open("rulz.txt"))

# Sort the values in descending order
sortedRules = sorted(rulesWithValues.items(), key=lambda x: -x[1])

# Create a list with only the rule's name
sortedRuleList = [x[0] for x in sortedRules]

# Create a dictionary with the rule name and function
rules = {'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'f': f}
### END OF DICTIONARYS ###

### READ file.CSV
dataset = pd.read_csv('servidorestable.csv',usecols=['hash_cpf','tempo_cargo','valor_bruto_mensal_para_o_mes_de_ref'])

total = int(dataset.hash_cpf.count())

###WRITE DATABASE_SERVER_CLASSIFICATION
with open('server_classification.csv', 'w', newline='') as csvfile:
    fieldnames = ['hash_cpf','classificacao']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in range(0,total):
        salarioVar = dataset.valor_bruto_mensal_para_o_mes_de_ref[row]
        salario = float(salarioVar.replace(',','.'))
        valorImovel = float(20000)###value default
        tempoDeServico = float(dataset.tempo_cargo[row])
        writer.writerow({'hash_cpf': dataset.hash_cpf[row], 'classificacao': str(indicador)})
       
        for rule in sortedRuleList:
            rules[rule]()

        with open('rulz.txt', 'w') as file:
            file.write(json.dumps(rulesWithValues))
        print ("Este servidor possui um indicador de " + str(indicador))
####
