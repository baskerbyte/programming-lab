i = 0
pEx = 0
troco = 0
total = 0

while i < 5:
    valor = float(input("Valor do item: "))
    pago = float(input("Valor pago pelo item: "))

    if valor > pago:
        print("Valor insuficiente, acrescente mais", valor - pago, "reais para completar a compra")
    else:
        total = total + valor

        if valor < pago:
            print("Valor superior, o troco será de", pago - valor, "reais")

            troco = troco + (pago - valor)
        else:
            print("Valor exato, não tem troco")

            pEx = pEx + 1
    
    i = i + 1
    

print("Pessoas que pagaram o valor exato:", pEx)
print("Total de troco recebido:", troco, "reais")
print("Total recebido:", total)