'''
2.	Exercicio02
a.	Crie uma lista constituída de “String” de caracteres.
b.	Faça a entrada de dados através do teclado.
c.	Ordene a lista
d.	Mostre os valores digitados nessa lista.
'''
lista = []

for c in range(10):
    lista.append(str(input('Insira o valor "String" a ser inserido na lista: ')))

print(lista)

input()