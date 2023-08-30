def calcula_nota(nota1, nota2, nota3, tipo):
    if tipo == "A":
        return (nota1 + nota2 + nota3) / 3
    elif tipo == "P":
        return (nota1 + nota2 + nota3) / 10
