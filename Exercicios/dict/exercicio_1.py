# Link Enunciado? https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true

from collections import Counter

# Counter me gera uma biblioteca com as ocorrencias como chave e os elementos
# da lista como valores


n_tenis_disponiveis = int(input())
lista_tamanhos_disponiveis = Counter(map(int,input().split(" ")))
n_clientes = int(input())
faturamento = 0 


# Lembrete -> map aplica uma função especifica em todos os elementos de um 
# iteravel

while n_clientes > 0:
    tamanho, preco = map(int,(input().split(" ")))
    if lista_tamanhos_disponiveis[tamanho] > 0:
        faturamento += preco
        lista_tamanhos_disponiveis[tamanho] -= 1 
    else:
        print("Tamanho {} indisponivel".format(tamanho))
    n_clientes -= 1

print("Faturamento: {}".format(faturamento))




'''
Argumentos de imput para
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
'''