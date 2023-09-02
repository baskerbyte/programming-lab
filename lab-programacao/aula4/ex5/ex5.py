'''
Implemente uma função chamada conta _ vogais que conte quantas vogais (a, e, i, o, u) há em uma string.
'''

def conta_vogais(string):
    cont = 0

    for i in string:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            cont += 1
    
    return cont
