# MC102L1 - Calcula o preço final de uma compra após um desconto relacionado ao dia do mês ou da semana e imprime diferentes mensagens de despedida a depender do dia da semana.

# Verifica se o dia do mês informado é um inteiro de 1 a 31.
while True:
    dia_mes_compra = input("Insira o dia do mês: ")
    try:
        dia_mes_compra = int(dia_mes_compra)
    except ValueError:
        print("Valor inválido! Ele deve ser um número inteiro de 1 a 31.")
    if type(dia_mes_compra) == int:
        if 31 >= dia_mes_compra >= 1:
            print("")
            break
        else:
            print("Valor inválido! Ele deve ser um número inteiro de 1 a 31.")

# Verifica se o dia da semana informado é válido.
while True:
    dia_semana_compra = input("Insira o dia da semana: ")
    dias_semana = {"segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"}
    if dia_semana_compra in dias_semana:
        print("")
        break
    else:
        print("Valor inválido! Ele deve ser, por exemplo, \"sexta-feira\", \"sábado\", etc..")

# Verifica se o preço inicial é um número racional não-negativo.
while True:
    valor_inicial = input("Insira o valor da compra sem desconto: ")
    try:
        valor_inicial = float(valor_inicial)
    except ValueError:
        print("Valor inválido! Ele deve ser um número racional não-negativo.")
    if type(valor_inicial) == float:
        if valor_inicial >= 0:
            print("")
            break
        else:
            print("Valor inválido! Ele deve ser um número racional não-negativo.")

# Define o valor final
if dia_mes_compra % 7 == 0:
    valor_final = round(0.5 * valor_inicial, 2)
elif dia_semana_compra == "sexta-feira":
    valor_final = round(0.25 * valor_inicial, 2)
else:
    valor_final = round(valor_inicial - dia_mes_compra, 2)

# Imprime o valor final
if valor_final < 0:
    print("0.00")
else:
    print(valor_final)

# Imprime a despedida
if dia_semana_compra == "sábado" or dia_semana_compra == "domingo":
    print("Agradecemos a preferência, tenha um ótimo fim de semana!")
elif dia_semana_compra == "segunda-feira":
    print("É um dia terrível, você não devia ter saído da cama.")
else:
    print(f"Agradecemos a preferência, tenha uma ótima {dia_semana_compra}!")