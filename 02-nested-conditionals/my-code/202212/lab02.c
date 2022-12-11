#include <stdio.h>
#include <string.h>

void meme_video(void) {
	printf("Quantos segundos são necessários para saber se um vídeo é bom?\n");
	int seconds;
	scanf("%d", &seconds);
	printf("%d\n", seconds);
	if (seconds < 0) {
		printf("Erro: entrada inválida\n");
		return;
	}
	printf("RESULTADO\n");
	if (seconds <= 5)
		printf("Você deveria estar no TikTok\n");
	else
		printf("Sua página de memes é: @meltmemes\n");
}

void capybaras(void) {
	printf("São as capivaras os melhores animais da Terra?\n");
	char capybaras[8];
	scanf("%s", capybaras);
	printf("%s\n", capybaras);
	if (strcmp(capybaras, "Sim") == 0) {
		printf("RESULTADO\n");
		printf("Sua página de memes é: @genteboamemes\n");
	}
	else if (strcmp(capybaras, "Não") == 0) {
		printf("RESULTADO\n");
		printf("Sua página de memes é: @wrongchoicememes\n");
	}
	else
		printf("Erro: entrada inválida\n");
}

void best_band(void) {
	printf("Qual banda você gosta mais?\n");
	char band;
	scanf(" %c", &band);
	switch (band) {
		case 'A':
			printf("A) Matanza\n");
			break;
		case 'B':
			printf("B) Iron Maiden\n");
			break;
		case 'C':
			printf("C) Imagine Dragons\n");
			break;
		case 'D':
			printf("D) BlackPink\n");
			break;
		default:
			printf("%c\n", band);
			printf("Erro: entrada inválida\n");
			return;
	}
	if (band == 'A' || band == 'B') {
		printf("RESULTADO\n");
		printf("Sua página de memes é: @badrockistamemes\n");
	} else if (band == 'C' || band == 'D')
		capybaras();
}

void family_group(void) {
	printf("Que imagem de bom dia você manda no grupo da família?\n");
	char good_morning[8];
	scanf(" %s", good_morning);
	if (strcmp(good_morning, "A") == 0) {
			printf("A) Bebê em roupa de flor\n");
			printf("RESULTADO\n");
			printf("Sua página de memes é: @bomdiabebe\n");
	}	else if	(strcmp(good_morning, "B") == 0) {
			printf("B) Gato\n");
			printf("RESULTADO\n");
			printf("Sua página de memes é: @kittykatmsgs\n");
	} else if (strcmp(good_morning, "C") == 0) {
			printf("C) Coração e rosas\n");
			printf("RESULTADO\n");
			printf("Sua página de memes é: @bomdiaflordodia\n");
	} else {
			printf("%s\n", good_morning);
			printf("Erro: entrada inválida\n");
	}
}

int main(void) {
	printf("*Que página de meme do Instagram você é?*\n");
	printf("Qual a sua idade?\n");
	int age;
	scanf("%d", &age);
	printf("%d\n", age);
	if (age < 0 || age > 125) {
		printf("Erro: entrada inválida\n");
		return 0;
	}
	if (age < 25)
		meme_video();
	else if (age < 41)
		best_band();
	else
		family_group();
	return 0;
}
