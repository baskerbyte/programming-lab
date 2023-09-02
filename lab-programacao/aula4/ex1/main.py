import ex1

lista = []

for _ in range(5):
    inpt = float(input("Digite um número: "))
    lista.append(inpt)

print(f'Maior número da lista: {ex1.encontra_maior(lista)}')