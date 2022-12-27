#include <stdio.h>
#include <stdlib.h>

void operate_modulo(int operand_1, int operand_2) {
	if (operand_1 == operand_2) {
		printf("0\n");
		return;
	}
	for (long int x = 1; x < abs(operand_1 - operand_2) + 1; x++)
		if ((operand_1 - operand_2) % x == 0)
			x != abs(operand_1 - operand_2) ? printf("%ld ", x) : printf("%ld\n", x);
}

int operate(char operator, long int operand_1, long int operand_2) {
	if (operator == '0')
		return 0;
	switch (operator) {
		case '+':
			printf("%ld\n", operand_1 + operand_2);
			break;
		case '-':
			printf("%ld\n", operand_1 - operand_2);
			break;
		case '*':
			printf("%ld\n", operand_1 * operand_2);
			break;
		case '/':
			printf("%ld %ld\n", operand_1 / operand_2, operand_1 % operand_2);
			break;
		case ';':
			operate_modulo(operand_1, operand_2);
			break;
	}
	return 1;
}

int main(void) {
	int resume = 1;
	while (resume) {
		char operator;
		long int operand_1, operand_2;
		scanf(" %c %ld %ld", &operator, &operand_1, &operand_2);
		resume = operate(operator, operand_1, operand_2);
	}
	return 0;
}
