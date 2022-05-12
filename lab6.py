from typing import List


class Room():
    def __init__(self, name: int, connections: List[int]) -> None:
        self._name = name
        self.connections = connections
        self._has_item = False

    @property
    def name(self) -> int:
        return self._name

    @name.setter
    def name(self, name: int) -> None:
        self._name = name

    def add_item(self, item: object):
        self.item = item
        self._has_item = True

    def has_item(self) -> bool:
        return self._has_item

    def remove_item(self) -> None:
        self.item = None
        self._has_item = False

    # def __str__(self):
    #     return self.name


class Entity():
    def __init__(self, room: object) -> None:
        self.room = room

    @property
    def room(self) -> object:
        return self._room

    @room.setter
    def room(self, room: object) -> None:
        self._room = room


class Item(Entity):
    def __init__(self, name: str, room: object) -> None:
        super().__init__(room)
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    # def store_in_player(self, player):
    #     self.room.name = (
    #         str(player.room.name) + " (inventário de " + player.name + ")"
    #     )


class NPC(Entity):
    def __init__(self, room: object) -> None:
        super().__init__(room)


class Player(Entity):
    def __init__(self, name: str, room: object) -> None:
        super().__init__(room)
        self.name = name
        self.is_alive = True
        self.inventory = []
        self.has_sword = False

    @property
    def is_alive(self) -> bool:
        return self._is_alive

    @is_alive.setter
    def is_alive(self, is_alive: bool) -> None:
        self._is_alive = is_alive

    @property
    def has_sword(self) -> bool:
        return self._has_sword

    @has_sword.setter
    def has_sword(self, has_sword: bool) -> None:
        self._has_sword = has_sword

    @property
    def inventory_size(self) -> int:
        return self._inventory_size

    @inventory_size.setter
    def inventory_size(self, inventory_size: int) -> None:
        self._inventory_size = inventory_size

    def describe_room(self) -> None:
        if self.room.has_item():
            print(
                "Você está na sala de número", self.room.name,
                "ela contém um baú com", self.room.item.name,
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
        print("Pegar", self.room.item.name)
        if not len(self.inventory) == self.inventory_size:
            print(self.room.item.name, "adicionado ao inventário")
            self.inventory.append(self.room.item)
            self.room.remove_item()
        else:
            print("Inventário cheio!")

    def drank_death_potion(self) -> bool:
        if self.inventory[-1].name == "poção":
            print(
                "Você pegou a poção da morte e virou pó instantaneamente. "
                "Tente novamente..."
            )
            return True
        else:
            return False


def generate_rooms():
    room_count = int(input())
    rooms = []
    for _ in range(room_count):
        room_and_connections = [int(i) for i in input().split()]
        rooms.append(Room(room_and_connections[0], room_and_connections[1:]))
    return rooms


def generate_items(rooms):
    item_count = int(input())
    items = []
    for _ in range(item_count):
        item_room, item_name = input().split()
        item_room = int(item_room)
        items.append(Item(item_name, rooms[item_room]))
        rooms[item_room].add_item(Item(item_name, rooms[item_room]))


def start_message():
    print(
        "Bem-vindo as Aventuras de Sarah 2.0\n"
        "Sarah acorda no saguão do antigo castelo de sua família,ela tem a"
        " oportunidade única de derrotar o seu clone maligno que se apoderou"
        " do reino.\n"
        "Para isso ela deve encontrar o baú da sua família que contém a"
        " espada mágica que apenas a verdadeira herdeira pode utilizar.\n"
        "Na sala onde está Sarah vê várias portas. Qual é a sua próxima ação?"
    )


def final_message(player):
    if player.has_sword:
        print(
            "Você derrotou o clone maligno com a espada mágica!"
            " Com a Sarah no reino o mundo pode voltar ao equilíbrio."
            "\nPARABÉNS!"
        )
    else:
        print(
            "Infelizmente você encontrou o clone sem a espada das "
            "fadas e foi derrotado. Tente novamente..."
        )


def main():
    rooms = generate_rooms()
    generate_items(rooms)
    clone = NPC(rooms[int(input())])
    bot = Player("bot", rooms[int(input())])
    bot.inventory_size = int(input())
    start_message()
    print("DEBUG - O clone está na sala:", clone.room.name)
    bot.describe_room()
    if bot.room.has_item():
        bot.try_to_store_item()
        bot.has_sword = bot.inventory[-1].name == "espada"
        bot.is_alive = not bot.drank_death_potion()
    if bot.is_alive:
        bot_path = input()
        bot_path = [int(i) for i in bot_path.split()]
        for i in bot_path:
            bot.room = rooms[i]
            print("Mover para sala", bot.room.name)
            if bot.room == clone.room:
                final_message(bot)
            else:
                bot.describe_room()
                if bot.room.has_item():
                    bot.try_to_store_item()
                    if bot.inventory[-1].name == "espada":
                        bot.has_sword = True
                    bot.drank_death_potion()


if __name__ == "__main__":
    main()
