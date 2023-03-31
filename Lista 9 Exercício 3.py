'''
3.	Exercicio03
a.	Crie uma lista de números inteiros
b.	Preencha a lista com 50 números aleatórios compreendidos entre 50 e 100;
c.	Mostre os valores da lista
d.	Mostre o maior valor entre eles (utilize a instrução for....)
e.	Mostre o menor valor entre eles. (utilize a instrução for....)
'''
import random

lista = []
maior = int
maiorTemp = 50
menor = int
menorTemp = 100

for c in range (50):
    lista.append(random.randint(50, 100))

for c in range (50):
    if lista[c] > maiorTemp:
        maior = maiorTemp
        maiorTemp = lista[c]

for c in range (50):
    if lista[c] < menorTemp:
        menor = menorTemp
        menorTemp = lista[c]

print(lista)
print('O maior valor é : ' + str(maior))
print('O menor valor é : ' + str(menor))


input()