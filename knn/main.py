import math
from typing import List, Any

import numpy as np
import csv
import pandas as pd

#def cos (x, y):
#def minkowski:

def escolha_linha_m(x, y):
    for i in range(len(x)):
        e.append(resu_manhanttan(x, y, i))
    return e


def escolha_linha_e(x, y):
    for i in range(len(x)):
        e.append(resu_euclidiana(x, y, i))
    return e

def manhanttan (x, y, q, n):
    m = []
    floatnumx = []
    floatnumy = []
    x = list(x)
    y = list(y)
    for i in range(len(x[0])):
        floatnumx.append(float(x[n][i]))
        floatnumy.append(float(y[q][i]))
    a = np.array(floatnumx)
    b = np.array(floatnumy)
    soma = 0
    m.append(abs(a - b))
    for z in range(len(x[0])):
        soma += m[z]
    return soma

def resu_manhanttan(x, y, n):
    resu = []
    indice = []
    count = 0
    min = 999999999
    for q in range(len(y)):
        resu.append(manhanttan(x, lista, q, n))
        if (resu[q] <= min).all():
            indice[count] = q
            min = resu[q]
            count += 1
    return indice


def euclidiana(x, y, q, n):
    m = []
    floatnumx = []
    floatnumy = []
    x = list(x)
    y = list(y)
    for i in range(len(x)):
        floatnumx.append(float(x[n][i]))
        floatnumy.append(float(y[q][i]))
    a = np.array(floatnumx)
    b = np.array(floatnumy)
    soma = 0
    m.append(abs(a - b)**2)
    for i in range(6):
        soma += m[i]
    return(soma**(1/2))


def resu_euclidiana(x, y, q):
    resu = []
    indice = []
    count = 0
    min = 999999999
    for q in range(len(y)):
        resu.append(euclidiana(x, y, q, n))
        if (resu[q] <= min).all():
            indice[count] = q
            min = resu[q]
            count += 1
    return indice


'''
def pearson (x, y):
    media_x = sum(x)/len(x)
    media_y = sum(y)/len(y)

    sub_media_x = [i - media_x for i in x]
    sub_media_y = [i - media_y for i in y]

    x_times_y = [a * b for a, b in list(zip(sub_media_x, sub_media_y))]

    x_squared = [i * i for i in x]
    y_squared = [i * i for i in y]

    return sum(x_times_y) / math.sqrt(sum(x_squared) * sum(y_squared))

'''

k =    #Aqui de define o k, podendo se 1, 3 ou 5

with open ("testes.csv", "r") as t:
    dadosteste = csv.reader(t, delimiter=";")
    listateste = list(dadosteste)


with open ("treino.csv", "r") as f:
    dados = csv.reader(f, delimiter=";")
    lista = list(dados)

'''

with open ("nome_testes.csv", "r") as p:
    dados_nome_testes = csv.reader(p, delimiter=";")
    lista_nome_testes = list(dados_nome_testes)
    
with open ("nomes_treinos.csv", "r") as r:
    dados_nome_treinos = csv.reader(r, delimiter=";")
    lista_nome_treinos = list(dados_nome_treinos)

manhanttan_list = escolha_linha_m(listateste, lista)
tamanho manhanttan = len(manhanttan_list)

euclidiana_list = escolha_linha_e(listateste, lista)
tamanho euclidiana = len(euclidiana_list)
'''

resu_m = []
resu_e = []
acerto_m = 0
acerto_e =0

if(k == 1):
    resu_m[0] = manhanttan_list[tamanho_manhanttan]
    resu_e[0] = euclidiana_list[tamanho_euclidiana]

if(k == 3):
    resu_m[0] = manhanttan_list[tamanho_manhanttan]
    resu_m[1] = manhanttan_list[tamanho_manhanttan - 1]
    resu_m[2] = manhanttan_list[tamanho_manhanttan - 2]
    resu_e[0] = euclidiana_list[tamanho_euclidiana]
    resu_e[1] = euclidiana_list[tamanho_euclidiana - 1]
    resu_e[2] = euclidiana_list[tamanho_euclidiana - 2]

if(k == 5):
    resu_m[0] = manhanttan_list[tamanho_manhanttan]
    resu_m[1] = manhanttan_list[tamanho_manhanttan - 1]
    resu_m[2] = manhanttan_list[tamanho_manhanttan - 2]
    resu_m[3] = manhanttan_list[tamanho_manhanttan - 3]
    resu_m[4] = manhanttan_list[tamanho_manhanttan - 4]
    resu_e[0] = euclidiana_list[tamanho_euclidiana]
    resu_e[1] = euclidiana_list[tamanho_euclidiana - 1]
    resu_e[2] = euclidiana_list[tamanho_euclidiana - 2]
    resu_e[3] = euclidiana_list[tamanho_euclidiana - 3]
    resu_e[4] = euclidiana_list[tamanho_euclidiana - 4]