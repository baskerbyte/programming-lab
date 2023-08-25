def calcula_imc(alt, sex):
    if sex == "H":
        return 72.7 * alt - 58
    else:
        return 62.1 * alt - 44.7
