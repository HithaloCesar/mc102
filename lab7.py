from typing import List


def without_equal_consecutive(list_: List[str]):
    """Dada uma lista de strings, retorna uma nova lista de strings com os
    mesmos elementos, mas sem elementos iguais consecutivos.
    """
    new_list = [list_[0]]
    for element in list_:
        if element != new_list[-1]:
            new_list.append(element)
    return new_list


def most_consecutive_occurrence(list_: List[str]):
    """Dada uma lista de strings, retorna o elemento que se mais se repete
    de forma consecutiva e quantas vezes ela se repete.
    """
    no_equal_consecutive = without_equal_consecutive(list_)
    element_count = []
    starting_index = 0
    for i in range(len(no_equal_consecutive)):
        element_count.append(0)
        for j in range(starting_index, len(list_)):
            if list_[j] == no_equal_consecutive[i]:
                element_count[i] += 1
                starting_index += 1
            else:
                break
    return (
        no_equal_consecutive[element_count.index(max(element_count))],
        (max(element_count))
    )


def remove_equal(list_: List[str]):
    """Dada uma lista de strings, retorna uma nova lista de strings com os
    mesmos elementos, mas sem repetição.
    """
    new_list = []
    for element in list_:
        if element not in new_list:
            new_list.append(element)
    return new_list


def count_unique_elements(list_: List[str]):
    """Dada uma lista de strings, retorna o número de elementos únicos na
    lista.
    """
    return len(remove_equal(list_))


def kebab_case_1_start(list_: List[str], start_after: str):
    """Dada uma lista de strings, converete seus elementos para kebab-case a
    partir de um caractere específico.
    """
    for element_index in range(len(list_)):
        renamed_element = ""
        start_conversion = False
        for char in list_[element_index]:
            if not start_conversion:
                renamed_element += char
                if char == start_after:
                    start_conversion = True
            else:
                if char.isupper():
                    char = char.lower()
                elif char == " ":
                    char = "-"
                renamed_element += char
        list_[element_index] = renamed_element


def main():
    photos_str, photo_to_remove = input().split("/ ")
    photos = photos_str.split(", ")
    most_consecutive_photo, count = most_consecutive_occurrence(photos)
    print(most_consecutive_photo, count)
    print(count_unique_elements(photos))
    photos = [
        photo for photo in photos if photo != photo_to_remove
    ]
    photos = remove_equal(photos)
    kebab_case_1_start(photos, "_")
    print([photo for photo in photos if photo[:2] == "HA"])
    print([photo for photo in photos if photo[:2] == "CR"])
    print([photo for photo in photos if photo[:2] == "CC"])


if __name__ == "__main__":
    main()
