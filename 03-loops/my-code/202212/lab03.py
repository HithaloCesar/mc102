from typing import Union


def ap_print(
		ap_constant: Union[int, float],
		start: Union[int, float],
		end: Union[int, float]) -> int:
	counter = 0
	current = start
	while current + ap_constant <= end:
		current += ap_constant
		print(current)
		counter += 1
	return counter


def main() -> None:
	# Requisição de dados:
	flask_count = int(input())
	metal_rate = float(input())
	solvent_constant = int(input())
	arithmetic_progression_constant = int(input())
	# Cálculo e impressão dos resultados de cada iteração a partir dos dados:
	metal_sub_total = 0
	for flask_index in range(1, flask_count + 1):
		metal_in_flask = metal_rate * flask_index + metal_rate * solvent_constant
		metal_sub_total += metal_in_flask
		print(flask_index, "%.2f" % metal_in_flask, "%.2f" % metal_sub_total)
	# Impressão da soma dos resultados calculados nas iterações:
	metal_total = metal_sub_total
	print("%.2f" % metal_total)
	# Impressão de uma progressão aritmética finita:
	counter = ap_print(arithmetic_progression_constant, 0, metal_total)
	# Impressão da quantidade de termos na progressão aritmética:
	print(counter)
	print("BATERIA DE TESTES TERMINADA")


if __name__ == "__main__":
	main()
