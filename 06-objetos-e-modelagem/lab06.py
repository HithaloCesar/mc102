from typing import List


class Room():
    """Representa uma sala, com suas conexões e seu item."""
    def __init__(self, name: int, connections: List[int]) -> None:
        self.name = name
        self.connections = connections
        self.item = None

    @property
    def item(self) -> str:
        """Retorna o nome do item."""
        return self._item

    @item.setter
    def item(self, item: str) -> None:
        """Define o nome do item."""
        self._item = item


class Entity():
    """Representa uma entidade.

    Aqui, entidade é algo que existe em uma sala.
    """
    def __init__(self, room: Room) -> None:
        self.room = room

    @property
    def room(self) -> Room:
        """Retorna o nome da sala."""
        return self._room

    @room.setter
    def room(self, room: Room) -> None:
        """Define o nome da sala."""
        self._room = room


class Player(Entity):
    """Representa um jogador, com um inventário.

    Capaz de armazenar itens no inventário, que inicia vazio e é limitado.
    """
    def __init__(self, room: Room) -> None:
        super().__init__(room)
        self.inventory = []
        self.has_sword = False

    @property
    def inventory_size(self) -> int:
        """Retorna o tamanho do inventário do jogador."""
        return self._inventory_size

    @inventory_size.setter
    def inventory_size(self, inventory_size: int) -> None:
        """Define o tamanho do inventário do jogador."""
        self._inventory_size = inventory_size

    @property
    def has_sword(self) -> bool:
        """Retorna o valor da variável has_sword.

        Essa variável define se o jogador possui a espada ou não.
        """
        return self._has_sword

    @has_sword.setter
    def has_sword(self, has_sword: bool) -> None:
        """Define o valor da variável has_sword."""
        self._has_sword = has_sword

    def describe_room(self) -> None:
        """Descreve a sala em que o jogador está situado.

        Cita o item e as conexões da sala.
        """
        if self.room.item is not None:
            print(
                "Você está na sala de número", self.room.name,
                "ela contém um baú com", self.room.item,
                "e dela você pode ir para as salas",
                self.room.connections
            )
        else:
            print(
                "Você está na sala de número", self.room.name,
                "e dela você pode ir para as salas",
                self.room.connections
            )

    def try_to_store_item(self) -> None:
        """Tenta mover o item da sala para o inventário do jogador."""
        if len(self.inventory) < self.inventory_size:
            print(self.room.item, "adicionado ao inventário")
            self.inventory.append(self.room.item)
            self.room.item = None
        else:
            print("Inventário cheio!")


def generate_rooms() -> List[Room]:
    """Dado um número p, permite a geração de p salas com conexões.

    Retorna uma lista (mapa) com os objetos sala gerados."""
    room_count = int(input())
    map_ = []
    for _ in range(room_count):
        room_and_connections = [int(i) for i in input().split()]
        map_.append(Room(room_and_connections[0], room_and_connections[1:]))
    return map_


def generate_items(map_: List[Room]) -> None:
    """Dado um número p, permite a geração de p itens em salas."""
    item_count = int(input())
    for _ in range(item_count):
        item_room, item_name = input().split()
        item_room = int(item_room)
        map_[item_room].item = item_name


def start_message() -> None:
    """Imprime a mensagem inicial do programa."""
    print(
        "Bem-vindo as Aventuras de Sarah 2.0\n"
        "Sarah acorda no saguão do antigo castelo de sua família,ela tem a"
        " oportunidade única de derrotar o seu clone maligno que se apoderou"
        " do reino.\n"
        "Para isso ela deve encontrar o baú da sua família que contém a"
        " espada mágica que apenas a verdadeira herdeira pode utilizar.\n"
        "Na sala onde está Sarah vê várias portas. Qual é a sua próxima ação?"
    )


def potion_message() -> None:
    """Imprime a mensagem de morte motivada pela poção."""
    print(
        "Você pegou a poção da morte e virou pó instantaneamente. Tente"
        " novamente..."
    )


def encounter_message(player: Player) -> None:
    """Imprime a mensagem de encontro com o clone.

    É otimista apenas se o jogador possuir a espada em seu inventário."""
    if player.has_sword:
        print(
            "Você derrotou o clone maligno com a espada mágica! Com a Sarah no"
            " reino o mundo pode voltar ao equilíbrio.\n"
            "PARABÉNS!"
        )
    else:
        print(
            "Infelizmente você encontrou o clone sem a espada das fadas e foi"
            " derrotado. Tente novamente..."
        )


def main():
    """Executa o programa principal."""
    map_ = generate_rooms()
    generate_items(map_)
    clone = Entity(map_[int(input())])
    bot = Player(map_[int(input())])
    bot.inventory_size = int(input())
    bot_path = input()
    bot_path = [int(i) for i in bot_path.split()]
    start_message()
    print("DEBUG - O clone está na sala:", clone.room.name)
    for i in range(len(bot_path) + 1):
        if bot.room != clone.room:
            bot.describe_room()
        if bot.room.item is not None:
            print("Pegar", bot.room.item)
            bot.try_to_store_item()
            if bot.inventory[-1] == "espada":
                bot.has_sword = True
            if bot.inventory[-1] == "poção":
                potion_message()
                break
        if bot.room == clone.room:
            encounter_message(bot)
        else:
            bot.room = map_[bot_path[i]]
            print("Mover para sala", bot.room.name)


if __name__ == "__main__":
    main()
