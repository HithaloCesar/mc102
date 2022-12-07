resultado = []
continua = True

while continua:
    result_parcial_mod = []
    operacao = input().split(" ")
    if len(operacao) == 3:
        operacao[1] = int(operacao[1])
        operacao[2] = int(operacao[2])
    if operacao[0] == "0":
        continua = False
    elif operacao[0] == "+":
        resultado.append(operacao[1] + operacao[2])
    elif operacao[0] == "-":
        resultado.append(operacao[1] - operacao[2])
    elif operacao[0] == "*":
        resultado.append(operacao[1] * operacao[2])
    elif operacao[0] == "/":
        resultado.append(str(operacao[1] // operacao[2]) + " " + str(operacao[1] % operacao[2]))
    elif operacao[1] == operacao[2]:
        resultado.append(0)
    else:
        for x in range(1, max([i for i in operacao if isinstance(i, int)])):
            if operacao[1] % x == operacao[2] % x:
                result_parcial_mod.append(x)
        resultado.append(" ".join(str(x) for x in result_parcial_mod))

for i in range(len(resultado)):
    print(resultado[i])