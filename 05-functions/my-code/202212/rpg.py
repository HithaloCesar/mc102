class RPGChar:

	def __init__(self, name: str, health: int, attack: int, defense: int,
	             x: str) -> None:
		self.name = name
		self.health = health
		self.attack = attack
		self.defense = defense
		self.x = x
		self.last_move = None
		self.special = False

	def soco(self, rpg: "RPG") -> None:
		rpg.seed_reroll()
		modifier = rpg.seed % 3
		damage = max(0, (self.attack - rpg.target.defense) * modifier)
		rpg.target.health -= damage
		rpg.event_print(rpg.target.name, "sofreu", damage, "dano")

	def arremesso_de_facas(self, rpg: "RPG") -> None:
		rpg.seed_reroll()
		hit_count = rpg.seed % 6
		damage = 0
		for hit_index in range(1, hit_count + 1):
			damage += self.attack // (3 ** hit_index)
		rpg.target.health -= damage
		rpg.event_print(rpg.target.name, "sofreu", damage, "dano")

	def _atk_or_def_up(self, rpg: "RPG", bonus: int) -> None:
		if bonus % 2 == 1:
			self.attack += bonus
			rpg.event_print(self.name, "ganhou", bonus, "ataque")
		else:
			self.defense += bonus
			rpg.event_print(self.name, "ganhou", bonus, "defesa")

	def invocacao_de_fada(self, rpg: "RPG") -> None:
		rpg.seed_reroll()
		hp_up = rpg.seed % 100
		rpg.seed_reroll()
		rpg.event_print(self.name, "ganhou", hp_up, "vida")
		bonus = rpg.seed % 1024
		if bonus < 100:
			self._atk_or_def_up(rpg, bonus)
		if bonus > 1018:
			rpg.user.special = True

	def execute_move(self, rpg: "RPG") -> None:
		match (self.last_move):
			case "soco":
				self.soco(rpg)
			case "facas":
				self.arremesso_de_facas(rpg)
			case "fada":
				self.invocacao_de_fada(rpg)


class RPG:

	def __init__(self, player: "RPGChar", enemy: "RPGChar",
	             seed: int) -> None:
		self.player = player
		self.enemy = enemy
		self.seed = seed
		self.player_turn = True
		self.battle_ended = False

	def set_user_target(self) -> None:
		if self.player_turn:
			self.user = self.player
			self.target = self.enemy
		else:
			self.user = self.enemy
			self.target = self.player

	def seed_reroll(self) -> None:
		self.seed = (7 * self.seed + 111) % 1024
		print(f"MENSAGEM DEBUG - número gerado: {self.seed}")

	def event_print(self, target: str, action: str, value: int,
	                stat: str) -> None:
		print(f"{target} {action} {value} pontos de {stat}!")

	def print_secret_ending(self) -> None:
		print("O quê? A fada trouxe um monstro gigante com ela!")
		if (self.player_turn):
			print(f"{self.enemy.name} e o castelo foram",
			      "destruídos,")
			print(f"e {self.player.name} agora tem um novo pet.")
			print("FINAL SECRETO - PARABENS???")
		else:
			print(f"{self.player.name} foi",
			      f"derrotad{self.player.x}...")
		self.battle_ended = True

	def print_regular_ending(self) -> None:
		if (self.player_turn):
			print(f"{self.enemy.name} foi derrotad{self.enemy.x}!",
			      f"{self.player.name} venceu!")
			print("FIM - PARABENS")
		else:
			print(f"{self.player.name} foi",
			      f"derrotad{self.player.x}...")
		self.battle_ended = True

	def check_battle_end(self) -> None:
		if self.user.special:
			self.print_secret_ending()
		elif self.player.health <= 0 or self.enemy.health <= 0:
			self.print_regular_ending()
