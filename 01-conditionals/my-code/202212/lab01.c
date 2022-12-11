#include <stdio.h>
#include <string.h>

int main(void) {
	// Requisição de dados:
  int month_day;
  scanf("%d", &month_day);
  char week_day[16];
  scanf("%s", week_day);
  double sub_total;
  scanf("%lf", &sub_total);
	// Cálculo dos resultados a partir dos dados:
  double total;
  if (month_day % 7 == 0)
    total = 0.5 * sub_total;
	else if (strcmp(week_day, "sexta-feira") == 0)
		total = 0.75 * sub_total;
	else
		total = sub_total - month_day;
	if (total < 0)
		total = 0;
	// Impressão dos resultados:
	printf("%.2lf\n", total);
	if (strcmp(week_day, "segunda-feira") == 0)
		printf("É um dia terrível, você não devia ter saído da cama.\n");
	else if (strcmp(week_day, "sábado") == 0 || strcmp(week_day, "domingo") == 0)
		printf("Agradecemos a preferência, tenha um ótimo fim de semana!\n");
	else
		printf("Agradecemos a preferência, tenha uma ótima %s!\n", week_day);
	return 0;
}
