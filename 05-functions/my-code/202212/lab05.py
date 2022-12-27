from rpg import *


def main() -> None:

	health, attack, defense = map(int, input().split())
	player = RPGChar("Sarah", health, attack, defense, "a")

	health, attack, defense = map(int, input().split())
	enemy = RPGChar("O clone", health, attack, defense, "o")

	seed = int(input())

	rpg = RPG(player, enemy, seed)

	while not rpg.battle_ended:
		rpg.set_user_target()

		rpg.user.last_move = input()
		rpg.user.execute_move(rpg)

		rpg.check_battle_end()
		rpg.player_turn = not rpg.player_turn


if __name__ == "__main__":
	main()
