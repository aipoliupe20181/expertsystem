#!/usr/bin/python
import json

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


### START LOOP ###
salario = input(str("Insira o valor do salario do servidor:"))
valorImovel = input(str("Insira o valor venal do imovel do servidor:"))
tempoDeServico = input(
    str("Insira o tempo (em meses) de servico do servidor:"))

for rule in sortedRuleList:
    rules[rule]()

# Save the rule's priority value in a text file
with open('rulz.txt', 'w') as file:
    file.write(json.dumps(rulesWithValues))

print "Este servidor possui um indicador de " + str(indicador)
### END  LOOP ###
