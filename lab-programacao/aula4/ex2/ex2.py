'''
    Crie uma função que encontre o maior e o menor elemento em uma lista de números.
'''

def maior_e_menor(lista):
    maior = lista[0]
    menor = lista[0]

    for item in lista:
        if item > maior:
            maior = item

        if item < menor:
            menor = item
    
    return (maior, menor)