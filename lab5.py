from typing import List


def create_char():
    """ Permite a criação de um personagem com os atributos HP, ATK e DEF."""
    char_stats = input().split()
    return [int(i) for i in char_stats]


def pseudorandom(random: int) -> int:
    """ Retorna um novo número pseudoaleatório, dado um anterior."""
    return (7 * random + 111) % 1024


def print_debug(random: int) -> int:
    """ Imprime uma mensagem debug."""
    print("MENSAGEM DEBUG - número gerado:", random)


def print_log(target: str, action: str, value: int, stat: str) -> None:
    """ Imprime o resultado de uma ação do round."""
    print(target, action, value, "pontos de", stat, end="!\n")


def soco(
        random: int, user_stats: List[int], target_stats: List[int],
        target: str) -> int:
    """ Aplica a habilidade "soco"."""
    random = pseudorandom(random)
    print_debug(random)
    m = random % 3
    if user_stats[1] - target_stats[2] > 0:
        damage = m * (user_stats[1] - target_stats[2])
        target_stats[0] -= damage
    else:
        damage = 0
    print_log(target, "sofreu", damage, "dano")
    return random


def arremesso_de_facas(
        random: int, user_stats: List[int], target_stats: List[int],
        target: str) -> int:
    """ Aplica a habilidade "arremesso de facas"."""
    random = pseudorandom(random)
    print_debug(random)
    n = random % 6
    damage = 0
    for i in range(1, n + 1):
        damage += user_stats[1] // 3 ** i
    target_stats[0] -= damage
    print_log(target, "sofreu", damage, "dano")
    return random


def invocacao_de_fada(
        random: int, user: str, user_stats: List[int], target_stats: List[int],
        player_turn: bool, target_secret_ending: str) -> int:
    """ Aplica a habilidade "invocação de fada"."""
    random = pseudorandom(random)
    print_debug(random)
    hp_up = random % 100
    user_stats[0] += hp_up
    random = pseudorandom(random)
    print_debug(random)
    print_log(user, "ganhou", hp_up, "vida")
    atk_def_up = random
    if atk_def_up < 100:
        if atk_def_up % 2 == 1:
            user_stats[1] += atk_def_up
            print_log(user, "ganhou", atk_def_up, "ataque")
        else:
            user_stats[2] += atk_def_up
            print_log(user, "ganhou", atk_def_up, "defesa")
    if atk_def_up >= 1019:
        target_stats[0] = 0
        print("O quê? A fada trouxe um monstro gigante com ela!")
        if player_turn:
            print(target_secret_ending, "e o castelo foram destruídos,")
            print("e", user, "agora tem um novo pet.")
            print("FINAL SECRETO - PARABENS???")
    return random


def verify_life_stats(
        user_stats: List[int], target_stats: List[int],
        random: int, target: str, user: str) -> bool:
    """ Verifica se a batalha terminou."""
    if user_stats[0] <= 0:
        print(target, "foi derrotada...")
        return False
    if target_stats[0] <= 0:
        if random < 1019:
            print(target, "foi derrotado!", user, "venceu!")
            print("FIM - PARABENS")
        return False
    else:
        return True


def main():
    Sarah_stats = create_char()
    clone_stats = create_char()
    random = int(input())
    player_turn = resume_battle = True
    target_secret_ending = "O Clone"
    while resume_battle:
        skill = input()
        if player_turn:
            user = "Sarah"
            user_stats = Sarah_stats
            target = "O clone"
            target_stats = clone_stats
        else:
            user = "O clone"
            user_stats = clone_stats
            target = "Sarah"
            target_stats = Sarah_stats
        if skill == "soco":
            random = soco(
                random, user_stats, target_stats, target
            )
        elif skill == "facas":
            random = arremesso_de_facas(
                random, user_stats, target_stats, target
            )
        elif skill == "fada":
            random = invocacao_de_fada(
                random, user, user_stats, target_stats,
                player_turn, target_secret_ending
            )
        resume_battle = verify_life_stats(
            Sarah_stats, clone_stats,
            random, target, user
        )
        player_turn = not player_turn


if __name__ == "__main__":
    main()
