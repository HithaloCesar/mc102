#include <stdio.h>

int ap_print(int ap_constant, int start, int end) {
	int counter = 0, current = start;
	while (current + ap_constant <= end) {
		current += ap_constant;
		printf("%d\n", current);
		counter++;
	}
	return counter;
}

int main(void) {
	// Requisição de dados:
	int flask_count;
	scanf("%d", &flask_count);
	double metal_rate;
	scanf("%lf", &metal_rate);
	int solvent_constant;
	scanf("%d", &solvent_constant);
	int ap_constant;
	scanf("%d", &ap_constant);
	// Cálculo e impressão dos resultados de cada iteração a partir dos dados:
	double metal_sub_total = 0;
	for (int flask_index = 1; flask_index < flask_count + 1; flask_index++) {
		double metal_in_flask = (
			metal_rate * flask_index + metal_rate * solvent_constant
		);
		metal_sub_total += metal_in_flask;
		printf("%d %.2lf %.2lf\n", flask_index, metal_in_flask, metal_sub_total);
	}
	// Impressão da soma dos resultados calculados nas iterações:
	double metal_total = metal_sub_total;
	printf("%.2lf\n", metal_total);
	// Impressão de parte de uma progressão aritmética:
	int counter = ap_print(ap_constant, 0, metal_total);
	// Impressão da quantidade de termos na progressão aritmética:
	printf("%d\n", counter);
	printf("BATERIA DE TESTES TERMINADA\n");
}
