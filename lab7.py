from typing import List, Tuple
# O professor Rafael Schouery autorizou a importação dessa biblioteca.


def longest_repetition(list_: List[str]) -> Tuple[str, int]:
    """Dada uma lista de strings, retorna a string que se mais se repete
    de forma consecutiva e quantas vezes ela se repete.
    """
    current_repetition = max_repetition = 1
    for i in range(len(list_) - 1):
        if list_[i] == list_[i + 1]:
            current_repetition += 1
        else:
            if current_repetition > max_repetition:
                max_repetition = current_repetition
                max_repetition_string = list_[i]
            current_repetition = 1
    return (
        max_repetition_string, max_repetition
    )


def set_(list_: List[str]) -> List[str]:
    """Dada uma lista de strings, retorna uma nova lista com as mesmas strings,
    mas sem repetição.
    """
    new_list = []
    for string in list_:
        if string not in new_list:
            new_list.append(string)
    return new_list


def kebab_case(list_: List[str], start_after: str) -> None:
    """Dada uma lista de strings, converete seus objetos para kebab-case a
    partir de um caractere específico.
    """
    for string_index in range(len(list_)):
        renamed_string = ""
        start_conversion = False
        for char in list_[string_index]:
            if not start_conversion:
                renamed_string += char
                if char == start_after:
                    start_conversion = True
            else:
                if char.isupper():
                    char = char.lower()
                elif char == " ":
                    char = "-"
                renamed_string += char
        list_[string_index] = renamed_string


def main():
    """Executa o programa principal."""
    photos_str, photo_to_remove = input().split("/ ")
    photos = photos_str.split(", ")
    most_consecutive_photo, count = longest_repetition(photos)
    print(most_consecutive_photo, count)
    photos = set_(photos)
    print(len(photos))
    photos = [
        photo for photo in photos if photo != photo_to_remove
    ]
    kebab_case(photos, "_")
    print([photo for photo in photos if photo[:2] == "HA"])
    print([photo for photo in photos if photo[:2] == "CR"])
    print([photo for photo in photos if photo[:2] == "CC"])


if __name__ == "__main__":
    main()
