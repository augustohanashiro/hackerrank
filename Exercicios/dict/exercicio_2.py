from collections import defaultdict


'''
link = https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true
será dado dois numeros inteiros n e m 
n = numero de palavras que pode ser repetida em um grupo A de palavras
m = nuemro de palabras que tera no grupo B. Para cada palavra em B, cheque quais
apareceram em A
printe os indices de cada palavra de B que aparece em A, se não aparecer nenhuma
retorne -1


entradas 
n e m separados por espaço
input das n palavras de entrda de A uma de cada vez
input das n palavras de entrda de B uma de cada vez

após isso, retornar as posições que cada item de b repetiu
'''

grupos = defaultdict(list)
n_elementos_a, m_elementos_b = map(int,input().split(" "))
indices_ocorrencias = ""
for indice in range(n_elementos_a):
    grupos["A"].append(input())
# print(grupos)

for indice in range(m_elementos_b):
    grupos["B"].append(input())
# print(grupos)

for elemento in grupos["B"]:
    if elemento in grupos["A"]:
        for indice in range(len(grupos["A"])):
            if elemento == grupos["A"][indice]:
                indices_ocorrencias += str(indice + 1) + " "
    else:
        indices_ocorrencias += -1 + " "
    indices_ocorrencias = indices_ocorrencias[:-1]  + "\n"

print(indices_ocorrencias[:-1])

