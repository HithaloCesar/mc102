# MC102L1 - Calcula o preço final de uma compra após um desconto relacionado ao dia do mês ou da semana e imprime diferentes mensagens de despedida a depender do dia da semana.

# Pede o dia do mês, que deve ser um número inteiro, o dia da semana, e o valor inicial da compra, que deve ser um número racional.
dia_mes_compra = int(input())
dia_semana_compra = input()
valor_inicial = float(input())

# Calcula o valor final da compra com base no dia do mês ou da semana.
if dia_mes_compra % 7 == 0:
    valor_final = round(0.5 * valor_inicial, 2)
elif dia_semana_compra == "sexta-feira":
    valor_final = round(0.75 * valor_inicial, 2)
else:
    valor_final = round(valor_inicial - dia_mes_compra, 2)
    if valor_final < 0:
        valor_final = 0

# Imprime o valor final da compra.
print("{:.2f}".format(valor_final))

# Imprime a mensagem de despedida a depender do dia da semana.
if dia_semana_compra == "sábado" or dia_semana_compra == "domingo":
    print("Agradecemos a preferência, tenha um ótimo fim de semana!")
elif dia_semana_compra == "segunda-feira":
    print("É um dia terrível, você não devia ter saído da cama.")
else:
    print(f"Agradecemos a preferência, tenha uma ótima {dia_semana_compra}!")
