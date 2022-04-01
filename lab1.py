# MC102L1 - Calcula o preço final de uma compra após um desconto relacionado ao dia do mês ou da semana e imprime diferentes mensagens de despedida a depender do dia da semana.

# Repete o programa após o fim de uma execução.
while True:

    # Pede o dia do mês e verifica se ele é um número inteiro de 1 a 31. Caso não seja, pergunta novamente.
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

    # Pede o dia da semana e verifica se ele é válido. Caso não seja, pergunta novamente.
    while True:
        dia_semana_compra = input("Insira o dia da semana: ")
        dias_semana = {"segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"}
        if dia_semana_compra in dias_semana:
            print("")
            break
        else:
            print("Valor inválido! Ele deve ser, por exemplo, \"sexta-feira\", \"sábado\", etc..")

    # Pede o valor inicial e verifica se ele é um número racional não-negativo. Caso não seja, pergunta novamente.
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

    # Define o valor final ao aplicar o desconto no valor inicial com base no dia do mês ou da semana.
    if dia_mes_compra % 7 == 0:
        valor_final = round(0.5 * valor_inicial, 2)
    elif dia_semana_compra == "sexta-feira":
        valor_final = round(0.75 * valor_inicial, 2)
    else:
        valor_final = round(valor_inicial - dia_mes_compra, 2)

    # Informa o valor final, que deve ser positivo e possuir dois dígitos após o separador decimal.
    if valor_final < 0:
        print("O valor final da compra é 0.00.")
    else:
        print("O valor final da compra é {:.2f}.".format(valor_final))

    # Imprime a despedida a depender do dia da semana e pula duas linhas para indicar o fim da execução.
    if dia_semana_compra == "sábado" or dia_semana_compra == "domingo":
        print("Agradecemos a preferência, tenha um ótimo fim de semana!\n\n")
    elif dia_semana_compra == "segunda-feira":
        print("É um dia terrível, você não devia ter saído da cama.\n\n")
    else:
        print(f"Agradecemos a preferência, tenha uma ótima {dia_semana_compra}!\n\n")
    
    # Insere uma linha de 20 hífens e pula duas linhas, para explicitar a reinicialização do programa.
    print(("-" * 20), "\n\n")