struct rpg_char {
	char name[8];
	int hp;
	int atk;
	int def;
	char x;
	int special;
	char last_move[8];
};

struct rpg {
	struct rpg_char *player;
	struct rpg_char *enemy;
	int seed;
	struct rpg_char *user;
	struct rpg_char *target;
	int player_turn;
	int battle_ended;
};


struct rpg_char * create_character(char *name, char x);

struct rpg * create_rpg(struct rpg_char *player, struct rpg_char *enemy,
                        int seed);

void set_user_target(struct rpg *g);

void execute_move(struct rpg *g);

void check_battle_end(struct rpg *g);
