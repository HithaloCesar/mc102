#include <stdio.h>
#include <stdlib.h>
#include "rpg.h"

int main(void)
{
	struct rpg_char *player, *enemy;
	struct rpg *g;
	int seed;

	player = create_character("Sarah", 'a');
	enemy = create_character("O clone", 'o');

	scanf("%d", &seed);

	g = create_rpg(player, enemy, seed);

	while (!g->battle_ended) {
		set_user_target(g);

		scanf("%s", g->user->last_move);
		execute_move(g);

		check_battle_end(g);
		g->player_turn = !g->player_turn;
	}

	free(player);
	free(enemy);
	free(g);

	return 0;
}
