#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include "rpg.h"

struct rpg_char * create_character(char *name, char x)
{
	int hp, atk, def;
	struct rpg_char *c;

	scanf("%d %d %d", &hp, &atk, &def);

	c = malloc(sizeof(struct rpg_char));
	strcpy(c->name, name);
	c->hp = hp;
	c->atk = atk;
	c->def = def;
	c->special = 0;
	c->x = x;

	return c;
}

struct rpg * create_rpg(struct rpg_char *player, struct rpg_char *enemy,
                        int seed) {
	struct rpg *g;

	g = malloc(sizeof(struct rpg));
	g->player = player;
	g->enemy = enemy;
	g->seed = seed;
	g->player_turn = 1;
	g->battle_ended = 0;

	return g;
}

void set_user_target(struct rpg *g)
{
	if (g->player_turn) {
		g->user = g->player;
		g->target = g->enemy;
	} else {
		g->user = g->enemy;
		g->target = g->player;
	}
}

void reroll_seed(struct rpg *g)
{
	g->seed = (7 * g->seed + 111) % 1024;
	printf("MENSAGEM DEBUG - número gerado: %d\n", g->seed);
}

void print_event(char *target, char *action, int value, char *stat)
{
	printf("%s %s %d pontos de %s!\n", target, action, value, stat);
}

void punch(struct rpg *g)
{
	int modifier, damage;

	reroll_seed(g);
	modifier = g->seed % 3;
	damage = (g->user->atk - g->target->def) * modifier;
	damage = damage > 0 ? damage : 0;
	g->target->hp -= damage;
	print_event(g->target->name, "sofreu", damage, "dano");
}

void throw_knives(struct rpg *g)
{
	int hit_count, damage, i;

	reroll_seed(g);
	hit_count = g->seed % 6;
	damage = 0;
	for (i = 1; i < hit_count + 1; i++)
		damage += g->user->atk / pow(3, i);
	g->target->hp -= damage;
	print_event(g->target->name, "sofreu", damage, "dano");
}

void raise_hp(struct rpg_char *user, int raise_value)
{
	user->hp += raise_value;
	print_event(user->name, "ganhou", raise_value, "vida");
}

void raise_atk(struct rpg_char *user, int raise_value)
{
	user->atk += raise_value;
	print_event(user->name, "ganhou", raise_value, "ataque");
}

void raise_def(struct rpg_char *user, int raise_value)
{
	user->def += raise_value;
	print_event(user->name, "ganhou", raise_value, "defesa");
}

void summon_fairy(struct rpg *g)
{
	int hp_up, bonus;

	reroll_seed(g);
	hp_up = g->seed % 100;
	reroll_seed(g);
	raise_hp(g->user, hp_up);
	bonus = g->seed % 1024;
	if (bonus < 100) {
		if (bonus % 2 == 1)
			raise_atk(g->user, bonus);
		else
			raise_def(g->user, bonus);
	} else if (bonus > 1018)
		g->user->special = 1;
}

void execute_move(struct rpg *g)
{
	if (strcmp(g->user->last_move, "soco") == 0)
		punch(g);
	else if (strcmp(g->user->last_move, "facas") == 0)
		throw_knives(g);
	else if (strcmp(g->user->last_move, "fada") == 0)
		summon_fairy(g);
}

void print_secret_ending(struct rpg *g)
{
	printf("O quê? A fada trouxe um monstro gigante com ela!\n");
	if (g->player_turn) {
		printf("%s e o castelo foram destruídos,\n", g->enemy->name);
		printf("e %s agora tem um novo pet.\n", g->player->name);
		printf("FINAL SECRETO - PARABENS???\n");
	} else
		printf("%s foi derrotad%c...\n", g->player->name, g->player->x);
	g->battle_ended = 1;
}

void print_regular_ending(struct rpg *g)
{
	if (g->player_turn) {
		printf("%s foi derrotad%c! ", g->enemy->name, g->enemy->x);
		printf("%s venceu!\n", g->player->name);
		printf("FIM - PARABENS\n");
	} else
		printf("%s foi derrotad%c...\n", g->player->name, g->player->x);
	g->battle_ended = 1;
}

void check_battle_end(struct rpg *g)
{
	if (g->user->special)
		return print_secret_ending(g);
	if (g->player->hp <= 0 || g->enemy->hp <= 0)
		return print_regular_ending(g);
}
