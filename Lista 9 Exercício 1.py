'''
1.	Exercicio01
a.	Crie uma lista de números inteiros
b.	Faça a entrada de 10 valores, digitados via teclado.
c.	Mostre os valores digitados na lista.
'''
lista = []

for c in range(10):
    lista.append(int(input('Insira o valor inteiro a ser inserido na lista: ')))

print(lista)
input()