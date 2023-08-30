nome = input("Nome do curso: ")
qtCompF = 0
mostL = 0
highestM = 0
highestC = ""

while nome != "sair":
    qtCand = int(input("Quantidade total de candidatos: "))
    num_vagas = int(input("Número de vagas: "))
    num_candM = int(input("Número de candidatos do sexo masculino: "))
    num_candF = qtCand - num_candM
    isFull = input("Preencheu todas as vagas? (S/N) ") == "S"

    if nome == "CC" or nome == "SI" or nome == "ES" or nome == "JG":
        qtCompF =  qtCompF + num_candF

    if num_vagas > 50:
        mostL = mostL + 1

    if num_candM > highestM:
        highestM = num_candM
        highestC = nome

    print("\n")
    nome = input("Nome do curso: ")

print("\n")
print("Quantidade de candidatos do sexo feminino no depertamento de computação:", qtCompF)
print("Quantidade de curso que oferecem mais que 50 vagas:", mostL)
print("Maior quantidade de homens no curso", highestC, "-", highestM)