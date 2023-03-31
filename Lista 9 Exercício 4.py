'''
4.	Exercicio04
a.	Crie 3 listas, lista1, lista2 e lista3 de números inteiros.
b.	Preencha a lista1 com 20 números aleatórios compreendidos entre 30 e 50.
c.	Preencha a lista2 com 30 números aleatórios compreendidos entre 50 e 70.
d.	Preencha a lista 3 com os elementos das listas lista1 e lista2, respectivamente 
e.	Mostre as listas
f.	Qual o maior número contido na lista3? Qual o menor? (utilize a instrução for...)
g.	Mostre a média aritmética dos valores contidos na lista3. (utilize a instrução for...)
'''
import random

lista1 = []
lista2 = []
lista3 = []
maior = int
maiorTemp = 20
menor = int
menorTemp = 50

for c in range(20):
    lista1.append(random.randrange(30,50))

for c in range(30):
    lista2.append(random.randrange(50,70))

lista3 = lista1 + lista2
medlista3 = ((sum(lista3) / 50))

for c in range(50):
    if lista3[c] > maiorTemp:
        maior = lista3[c]
        maiorTemp = maior
    if lista3[c] < menorTemp:
        menor = lista3[c]
        menorTemp = menor

print('Lista 1 = ' + str(lista1))
print('Lista 2 = ' + str (lista2))
print('Lista 3 = ' + str(lista3))
print('O maior número da lista 3 é = ' + str(maior))
print('O menor número da lista 3 é = ' + str(menor))
print('A média aritmética da lista 3 é = '+ str(medlista3))
input()