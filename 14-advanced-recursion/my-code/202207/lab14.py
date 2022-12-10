from typing import List


def set_matrix(n: int) -> List[List[int]]:
    """Permite a inserção de uma matriz quadrada n x n.

    Dado o tamanho de uma matriz n x n, permite a inserção de suas entradas.

    Args:
        n:
            Tamanho da matriz quadrada a ser inserida.

    Returns:
        Uma matriz quadrada.
    """
    matrix = []
    for _ in range(n):
        line = [int(entry) for entry in input().split()]
        matrix.append(line)
    return matrix


def get_determinant_product(
        matrix: List[List[int]],
        determinant: int =1) -> int:
    """Multiplica um determinante com o determinante de uma matriz n x n.

    Inicializa o cálculo do produto de um determinante pelo determinante
    de uma matriz quadrada. Também pode calcular o determinante de qualquer
    matriz quadrada ao utilizar o elemento identidade da multiplicação como
    determinante inicial.

    Args:
        matrix:
            Matriz quadrada cujo determinante será utilizado para calcular o
            produto de determinantes.
        determinant:
            Valor inicial do determinante, que será utilizado para calcular o
            produto de determinantes.

    Returns:
        Produto do determinante inicial com o determinante da matriz quadrada.
    """
    determinant *= get_matrix_determinant(matrix)
    return determinant


def get_matrix_determinant(matrix: List[List[int]]) -> int:
    """Calcula recursivamente o determinante de uma matriz quadrada.

    Por meio da expansão de Laplace, obtém o determinante de uma matriz
    quadrada.

    Args:
        matrix:
            Matriz quadrada cujo determinante será calculado.

    Returns:
        determinant:
            Valor calculado para o determinante.
    """
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    determinant = 0
    for line in range(len(matrix)):
        minor_matrix = get_minor_matrix(matrix, line, 0)
        determinant += (
            (-1) ** (line + 0)
            * matrix[line][0]
            * get_matrix_determinant(minor_matrix)
        )
    return determinant


def get_minor_matrix(
        matrix: List[List[int]],
        i: int,
        j: int) -> List[List[int]]:
    """Obtém a matriz cujo determinante é o menor complementar de a_{i, j}.

    Dada uma matriz quadrada, além da linha e da coluna da entrada cujo menor
    complementar deve ser calculado, retorna o menor complementar dessa
    entrada.

    Args:
        matrix:
            Matriz quadrada de onde a matriz cujo determinante é o menor
            complementar será obtido.
        i:
            Linha a ser eliminada para gerar a matriz cujo determinante é o
            menor complementar da entrada a_{i, j}.
        j:
            Coluna a ser eliminada para gerar a matriz cujo determinante é o
            menor complementar da entrada a_{i, j}.

    Returns:
        Matriz cujo determinante é o menor complementar da entrada a_{i, j}.
    """
    minor = []
    for line in range(len(matrix)):
        if line != i:
            minor.append([])
            for column in range(len(matrix[line])):
                if column != j:
                    minor[len(minor) - 1].append(matrix[line][column])
    return minor


def main():
    """Executa o programa principal."""
    matrix_count = int(input())
    n = int(input())
    determinant = 1
    for _ in range(matrix_count):
        matrix = set_matrix(n)
        determinant = get_determinant_product(matrix, determinant)
    final_message = (
        f"Após as {matrix_count} transformações, o objeto {n}-dimensional"\
        f" teve o volume multiplicado no valor {determinant}."
    )
    print(final_message)


if __name__ == "__main__":
    main()
