import ex2

lista = []

for _ in range(5):
    inpt = float(input("Digite um número: "))
    lista.append(inpt)

(maior, menor) = ex2.maior_e_menor(lista)

print(f'Maior número da lista: {maior}\nMenor número da lista: {menor}')
