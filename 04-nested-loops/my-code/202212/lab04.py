def operate_modulo(operand_1: int, operand_2: int) -> None:
	if operand_1 == operand_2:
		print(0)
		return
	for x in range(1, abs(operand_1 - operand_2) + 1):
		if (operand_1 - operand_2) % x == 0:
			print(x, end = " ") if x != abs(operand_1 - operand_2) else print(x)


def operate(operator: str, operand_1: int, operand_2: int) -> bool:
	if operator == "0":
		return False
	match operator:
		case "+":
			print(operand_1 + operand_2)
		case "-":
			print(operand_1 - operand_2)
		case "*":
			print(operand_1 * operand_2)
		case "/":
			print(operand_1 // operand_2, operand_1 % operand_2)
		case ";":
			operate_modulo(operand_1, operand_2)
	return True


def main() -> None:
	resume = True
	while resume:
		operator, operand_1, operand_2 = input().split()
		operand_1 = int(operand_1)
		operand_2 = int(operand_2)
		resume = operate(operator, operand_1, operand_2)


if __name__ == "__main__":
	main()
