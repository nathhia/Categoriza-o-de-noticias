#Nathalia Albuquerque e Dhavid Douglas
#Projeto de inteligencia artiicial


sport = [3786]
business = [3496]
politics = [3541]
tech = [3975]
intertainment = [3696]
entrada = []
''''
count_sport
count_tech
count_business
count_politics
count_intertainment
'''

import csv

arquivo = open('sport.csv')

linhas = csv.reader(arquivo)

for linha in linhas:
    sport.append(linha)

import csv

arquivo = open('tech.csv')

linhas = csv.reader(arquivo)

for linha in linhas:
    tech.append(linha)

import csv

arquivo = open('politics.csv')

linhas = csv.reader(arquivo)

for linha in linhas:
    politics.append(linha)

import csv

arquivo = open('business.csv')

linhas = csv.reader(arquivo)

for linha in linhas:
    business.append(linha)

import csv

arquivo = open('intertainment.csv')

linhas = csv.reader(arquivo)

for linha in linhas:
    intertainment.append(linha)



'''
for x in tech
    for y in entrada
        if tech[x] == entrada[y]:
            count_tech++

for x in politics
    for y in entrada
        if politics[x] == entrada[y]:
            count_politics++

for x in sport
    for y in entrada
        if sport[x] == entrada[y]:
            count_sport++

for x in business
    for y in entrada
        if business[x] == entrada[y]:
            count_business++

for x in intertainment
    for y in entrada
        if intertainment[x] == entrada[y]:
            count_intertainment++

'''