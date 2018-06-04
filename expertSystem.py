#!/usr/bin/python

### START OF RULES ###

def ge():
    if(salario > valorImovel):
        print "salario e maior"
        rulesWithValues['g'] +=1

def he():
    if(salario < valorImovel):
        print "salario e menor"
        rulesWithValues['h'] +=1

def ie():
    if(salario == valorImovel):
        print "igual"
        rulesWithValues['i'] +=1

### END OF RULES ###

file = open("rules.txt", "r")
#for line in file:
    #loadRules(line)

### START OF DICTIONARYS ###
rulesWithValues = {'g': 0, 'h': 0, 'i': 0}

sortedRules = sorted(rulesWithValues.items(), key=lambda x: -x[1])

sortedRuleList = [x[0] for x in sortedRules]

func = {'g': ge, 'h': he, 'i': ie}

### END OF DICTIONARYS ###


### START LOOP ###
for x in range(0,5):

    salario=input(str("Salario:"))
    valorImovel = input(str("Imovel:"))

    print rulesWithValues
    print sortedRules
    print sortedRuleList

    for rule in sortedRuleList:
        func[rule]()
        print rulesWithValues
    
### END  LOOP ###