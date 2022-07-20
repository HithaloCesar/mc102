"""Editor simples de imagens em escala de cinza.

Esse módulo é um editor de imagens simples em escala de cinza com as operações
seleção retangular, espelhamento (horizontal ou vertical), cópia, recorte e
rotação de 90 graus no sentido horário.
"""


from typing import List, Optional, Union


class Matrix:
    def __init__(self, matrix: List[Optional[List[int]]]):
        """Gera uma matriz.

        Inicialmente, toda a matriz está selecionada como uma submatriz.
        """
        self.matrix = matrix
        self.sub_00_x = 0
        self.sub_00_y = 0
        self.sub_h = len(self.matrix)
        try:
            self.sub_w = len(self.matrix[0])
        except IndexError:
            self.sub_w = 0

    def add_row(self, new_row: List[int]):
        """Adiciona uma nova linha ao fim de uma matriz.

        Args:
            new_row:
                Lista de inteiros a ser adicionada na matriz.
        """
        self.matrix.append(new_row)
        self.sub_h += 1
        self.sub_w = len(self.matrix[0])

    def select(
            self,
            sub_00_x: Union[str, int],
            sub_00_y: Union[str, int],
            sub_w: Union[str, int],
            sub_h: Union[str, int]) -> None:
        """Seleciona uma submatriz.

        Args:
            sub_00_x:
                Índice da coluna (x) do primeiro objeto (0, 0) da submatriz.
            sub_00_y:
                Índice da linha (y) do primeiro objeto (0, 0) da submatriz.
            sub_w:
                Largura (width) da submatriz.
            sub_h:
                Altura (height) da submatriz.
        """
        selection_data = [sub_00_x, sub_00_y, sub_w, sub_h]
        self.sub_00_x, self.sub_00_y, self.sub_w, self.sub_h = \
            [int(data) for data in selection_data]

    def mirror(self, option: str) -> None:
        """Espelha uma submatriz horizontalmente ou verticalmente.

        Args:
            option:
                "h" para espelhar horizontalmente.
                "v" para espelhar verticalmente.
        """
        if option == "h":
            self.mirror_horizontally()
        elif option == "v":
            self.mirror_vertically()

    def mirror_horizontally(self) -> None:
        """Espelha uma submatriz horizontalmente."""
        last_sub_col = self.sub_00_x + self.sub_w
        for line in range(self.sub_00_y, self.sub_00_y + self.sub_h):
            self.matrix[line][self.sub_00_x:last_sub_col] = \
                list(reversed(self.matrix[line][self.sub_00_x:last_sub_col]))

    def mirror_vertically(self) -> None:
        """Espelha uma submatriz verticalmente."""
        for column in range(self.sub_00_x, self.sub_00_x + self.sub_w):
            for line in range(self.sub_00_y, self.sub_00_y + self.sub_h // 2):
                dynamic_last_line = \
                    self.sub_00_y + (self.sub_h - 1) - (line - self.sub_00_y)
                aux = self.matrix[line][column]
                self.matrix[line][column] = \
                    self.matrix[dynamic_last_line][column]
                self.matrix[dynamic_last_line][column] = aux

    def copy(self) -> "Matrix":
        """Copia uma submatriz.

        Returns:
            Um objeto matrix, ou seja, uma matriz, que é a submatriz copiada.
        """
        submatrix = Matrix([])
        last_sub_col = self.sub_00_x + self.sub_w
        for line in range(self.sub_00_y, self.sub_00_y + self.sub_h):
            submatrix.add_row(self.matrix[line][self.sub_00_x:last_sub_col])
        return submatrix


    def cut(self, empty: int) -> "Matrix":
        """Recorta uma submatriz.

        Com base na seleção atual, uma submatriz é gerada e trocam-se as
        entradas da seleção na matriz original por valores que representam um
        vazio.

        Args:
            empty:
                Número inteiro que representa um objeto nulo na matriz.

        Returns:
            Um objeto matrix, ou seja, uma matriz, que é a submatriz
            recortada.
        """
        submatrix = Matrix([])
        last_sub_col = self.sub_00_x + self.sub_w
        for line in range(self.sub_00_y, self.sub_00_y + self.sub_h):
            submatrix.add_row(self.matrix[line][self.sub_00_x:last_sub_col])
            self.matrix[line][self.sub_00_x:last_sub_col] = \
                [empty for _ in range(self.sub_w)]
        return submatrix

    def rotate_90_clockwise(self, empty: int) -> "Matrix":
        """Recorta uma submatriz e a rotaciona 90 graus no sentido horário.

        Args:
            empty:
                Número inteiro que representa um objeto nulo na matriz.

        Returns:
            Um objeto matrix, ou seja, uma matriz, que é a submatriz
            rotacionada.
        """
        submatrix = Matrix([])
        last_sel_line = self.sub_00_y + self.sub_h - 1
        for column in range(self.sub_00_x, self.sub_00_x + self.sub_w):
            submatrix.add_row([])
            for line in range(last_sel_line, self.sub_00_y - 1, -1):
                submatrix.matrix[column - self.sub_00_x].append(
                    self.matrix[line][column]
                )
                self.matrix[line][column] = empty
        return submatrix

    def paste(
            self,
            submatrix: "Matrix",
            paste_00_x: Union[str, int],
            paste_00_y: Union[str, int]) -> None:
        """Cola uma submatriz em uma matriz.

        Sobrescreve entradas de uma matriz com entradas de uma submatriz.
        Restringe-se a casos em que a matriz, após colagem da submatriz,
        possui as mesmas dimensões da matriz original.

        Args:
            submatrix:
                É uma instanciação da classe Matrix e é a submatriz a ser
                colada.
            paste_00_x:
                Índice da coluna (x) do objeto da matriz localizado na posição
                que o primeiro objeto da submatriz será colado.
            paste_00_y:
                Índice da linha (y) do objeto da matriz localizado na posição
                que o primeiro objeto da submatriz será colado.
        """
        paste_00_x, paste_00_y = [int(x) for x in [paste_00_x, paste_00_y]]
        for line in range(len(submatrix.matrix)):
            current_paste_line = paste_00_y + line
            last_column = paste_00_x+len(submatrix.matrix[0])
            self.matrix[current_paste_line][paste_00_x:last_column] = \
                submatrix.matrix[line]

    def __str__(self):
        return str("\n".join(
            [" ".join([f"{obj:03}" for obj in row]) for row in self.matrix]
        ))


def main():
    """Executa o programa principal."""
    image = Matrix([])
    image_w, image_h = [int(entry) for entry in input().split()]
    operation_count = int(input())
    for _ in range(image_h):
        image.add_row([int(entry) for entry in input().split()])
    for _ in range(operation_count):
        entry = input().split()
        operation = entry[0]
        if operation == "selecao":
            sel_00_x, sel_00_y, sel_w, sel_h = entry[1:]
            image.select(sel_00_x, sel_00_y, sel_w, sel_h)
        elif operation == "espelhamento":
            orientation = entry[1]
            image.mirror(orientation)
        elif operation == "copia":
            paste_00_x, paste_00_y = entry[1:]
            sel_copy = image.copy()
            image.paste(sel_copy, paste_00_x, paste_00_y)
        elif operation == "recorte":
            paste_00_x, paste_00_y = entry[1:]
            sel_copy = image.cut(0)
            image.paste(sel_copy, paste_00_x, paste_00_y)
        elif operation == "rotacao":
            rotated_sel = image.rotate_90_clockwise(0)
            image.paste(rotated_sel, image.sub_00_x, image.sub_00_y)
    print(image, end="")


if __name__ == "__main__":
    main()
