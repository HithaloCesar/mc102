"""Organizador de arquivos.

Esse módulo organiza arquivos do sistema com base em seus caminhos relativos.
"""


def sort_file_rec(files, main_folder, file, index):
    """Via recusão, retorna o caminho do arquivo até a pasta principal.

    Args:
        files:
            Lista de arquivos do sistema com os respectivos diretórios.
        main_folder:
            Nome da pasta principal, que contém todos os demais arquivos do
            sistema.
        file:
            Arquivo do sistema a ser procurado em files.
        index:
            Índice decrescente para a procura em files.

    Returns:
        O caminho do arquivo, separado por underscores.
    """
    file_sys, location = files[index].split()
    if file != file_sys:
        return sort_file_rec(files, main_folder, file, index - 1)
    elif location != main_folder:
        return sort_file_rec(files, main_folder, location, index - 1) + "_" + file_sys
    else:
        return location + "_" + file_sys


def sort_file(files, main_folder):
    """Casca para a função recursiva de organização de arquivos.

    Args:
        files:
            Lista de arquivos do sistema com os respectivos diretórios.
        main_folder:
            Nome da pasta principal, que contém todos os demais arquivos do
            sistema.

    Returns:
        O retorno da função recursiva de organização de arquivos.
    """
    file = files[-1].split()[0]
    return sort_file_rec(files, main_folder, file, -1)


def main():
    """Executa o programa principal."""
    main_folder, file_sys_count = input().split()
    file_sys_count = int(file_sys_count)
    files = []
    for counter in range(file_sys_count):
        entry = input()
        files.append(entry)
        path = sort_file(files, main_folder)
        print(path, end="")
        if counter != file_sys_count - 1:
            print()
    print()


if __name__ == "__main__":
    main()
