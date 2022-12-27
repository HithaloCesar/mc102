def main() -> None:
	# Requisição de dados:
	month_day = int(input())
	week_day = input()
	sub_total = float(input())
	# Cálculo dos resultados a partir dos dados:
	if month_day % 7 == 0:
		total = 0.5 * sub_total
	elif week_day == "sexta-feira":
		total = 0.75 * sub_total
	else:
		total = sub_total - month_day
	if total < 0:
		total = 0
	# Impressão dos resultados:
	print("%.2f" % total)
	if week_day == "segunda-feira":
		print("É um dia terrível, você não devia ter saído da cama.")
	elif week_day == "sábado" or week_day == "domingo":
		print("Agradecemos a preferência, tenha um ótimo fim de semana!")
	else:
		print(f"Agradecemos a preferência, tenha uma ótima {week_day}!")


if __name__ == "__main__":
	main()
