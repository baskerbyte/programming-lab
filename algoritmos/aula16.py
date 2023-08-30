produtos = [
    ['Smartphone', 1000.00, 10],
    ['Notebook', 2000.00, 5],
    ['Teclado', 200.00, 20],
    ['Televisão', 1500.00, 3],
    ['Tablet', 500.00, 15]
]
cod = int(input("Digite um código: "))

while cod != 5:
    i = 0
    if cod == 1:
        nome = input("Digite um nome do produto: ")
        preco = int(input("Digite o preço do produto: "))
        qt = int(input("Digite a quantidade do produto: "))

        produtos.append([nome, preco, qt])
        print("------------")
    elif cod == 2:
        while i < len(produtos):
            produto = produtos[i]
            print("Nome:", produto[0], "Valor do estoque:", produto[1] * produto[2])
            i = i + 1
        print("------------")
    elif cod == 3:
        soma = 0
        while i < len(produtos):
            soma = soma + produtos[i][1]
            i = i + 1
        print("Média:", soma / len(produtos))
    elif cod == 4:
        print("------------")
        pr = []
        while i < len(produtos):
            produto = produtos[i]
            if produto[2] < 10:
                pr.append([produto[0], produto[2]])
            i = i + 1
        i = 0
        while i < len(pr):
            produto = pr[i]
            print("Nome:", produto[0], "Quantidade:", produto[1], "Quantidade para atingir 50:", 50 - produto[1])
            i = i + 1
        print("------------")
    cod = int(input("Digite um código: "))