"""Calculador de melhor rota possível para um robô engregador.

Esse módulo calcula, com base em distâncias e parâmetros quânticos e
relativísticos, a melhor rota possível para um robô entregador interplanetário
realizar a entrega de lanches. Antimatéria é o combustível do robô, e seu
tanque possui capacidade de 50.0 hawkings.
"""


from decimal import getcontext, Decimal
from typing import Dict, Tuple, Union
import recipes_decimal


def binary_search(
        pi: Decimal,
        a: Decimal,
        b: Decimal,
        c: Decimal,
        d: Decimal,
        searched_distance: Decimal) -> Union[Decimal, int]:
    """Executa a busca binária da quantidade de antimatéria a ser utilizada.

    Dado uma distância e os devidos parâmetros da fórmula responsável pelo
    cálculo da distância, realiza uma busca binária a fim de encontrar a
    correta quantidade de antimatéria a ser utilizada como combustível.

    Args:
        pi:
            O número pi, com um número determinado de casas decimais.
        a:
            Variável a da fórmula da distância.
        b:
            Variável b da fórmula da distância.
        c:
            Variável c da fórmula da distância.
        d:
            Variável d da fórmula da distância.
        searched_distance:
            Distância-alvo, a qual a busca binária deve encontrar.

    Returns:
        A quantidade de antimatéria a ser utilizada na rota ou -1, caso não
        encontre a distância desejada.
    """
    left = Decimal(0)
    right = Decimal(50)
    while left <= right:
        middle = (left + right) / 2
        distance = distance_formula(pi, a, b, c, d, middle)
        if abs(left - right) < Decimal(10) ** -32:
            return middle
        elif distance < searched_distance:
            left = middle
        else:
            right = middle
    return -1


def zeta_function(
        pi: Decimal,
        b: Decimal,
        x: Decimal) -> Decimal:
    """Calcula a função zeta.

    Dadas as devidas variáveis, calcula a função zeta, utilizada, por exemplo,
    na fórmula da distância.

    Args:
        pi:
            O número pi, com um número determinado de casas decimais.
        b:
            Variável b da fórmula da distância.
        x:
            Quantidade de antimatéria a ser utilizada na rota.

    Returns:
        O valor calculado para zeta.
    """
    zeta = Decimal(0)
    for i in range(1, 101):
        zeta += Decimal(1) / (Decimal(i) ** (b * x + pi))
    return zeta


def distance_formula(
        pi: Decimal,
        a: Decimal,
        b: Decimal,
        c: Decimal,
        d: Decimal,
        x: Decimal) -> Decimal:
    """Calcula a fórmula da distância.

    Dados as devidas variáveis, calcula a distância possível para uma
    determinada quantidade de antimatéria como combustível.

    Args:
        pi:
            O número pi, com um número determinado de casas decimais.
        a:
            Variável a da fórmula da distância.
        b:
            Variável b da fórmula da distância.
        c:
            Variável c da fórmula da distância.
        d:
            Variável d da fórmula da distância.
        x:
            Quantidade de antimatéria a ser utilizada na rota.

    Returns:
        O valor calculado para a distância.
    """
    zeta = zeta_function(pi, b, x)
    y = (pi + a * Decimal(x).exp() - Decimal(zeta)) / (Decimal(-Decimal.sqrt(c * x)).exp() + d * (2 * pi ** 3 - x))
    return y


def read_data(routes_count: int) -> Tuple[Dict[str, Decimal], Decimal]:
    """Permite a inserção de dados no programa.

    Lê os nomes dos planetas, suas distâncias e os parâmetros quânticos e
    relativísticos a serem empregados no cálculo da quantidade de antimatéria
    a ser utilizada para o deslocamento.

    Args:
        routes_count:
            Quantidade de rotas possíveis.

    Returns:
        Um dicionário de planetas e suas respectivas distâncias, e os
        parâmetros quânticos e relativísticos (a, b, c, d).
    """
    distances = {}
    for _ in range(routes_count):
        planet = input()
        distance = Decimal(input())
        distances[planet] = distance
    a = Decimal(input())
    b = Decimal(input())
    c = Decimal(input())
    d = Decimal(input())
    return distances, a, b, c, d


def print_setter(
        distances: Dict[str, Decimal],
        max_distance: Decimal,
        min_distance: Decimal) -> Tuple[bool, Union[None, str],\
            Union[None, Decimal]]:
    """Determina a impressão a ser realizada.

    Com base nas restrições do tanque de combustível, determina a melhor rota
    possível para o robô entregador, que deverá ser impressa.

    Args:
        distances:
            Dicionário com os nomes de planetas e suas respectivas distâncias.
        max_distance:
            Distância máxima possível com o tanque de combustível do robô.
        min_distance:
            Distância mínima possível.

    Returns:
        A possibilidade ou não do robô realizar uma entrega, dadas as rotas
        possíveis; o nome do planeta com a melhor rota; a distância do
        respectivo planeta.
    """
    can_deliver = False
    optimal_distance_planet = None
    optimal_distance = None
    for planet, distance in distances.items():
        if max_distance >= distance >= min_distance:
            if not can_deliver:
                optimal_distance_planet = planet
                optimal_distance = distance
            elif distance > optimal_distance:
                optimal_distance_planet = planet
                optimal_distance = distance
            can_deliver = True
    return can_deliver, optimal_distance_planet, optimal_distance


def print_data(
        can_deliver: bool,
        pi: Decimal,
        a: Decimal,
        b: Decimal,
        c: Decimal,
        d: Decimal,
        optimal_distance_planet: str,
        optimal_distance: Decimal) -> None:
    """Imprime a ação realizada pelo robô entregador.

    Dados as devidas informações e parâmetros, imprime a rota escolhida pelo
    robô ou a ação de "dar um grau", caso nenhuma rota seja possível.

    Args:
        can_deliver:
            Possibilidade ou não do robô entregador utilizar uma das rotas
            informadas.
        pi:
            O número pi, com um número determinado de casas decimais.
        a:
            Variável a da fórmula da distância.
        b:
            Variável b da fórmula da distância.
        c:
            Variável c da fórmula da distância.
        d:
            Variável d da fórmula da distância.
        optimal_distance_planet:
            Nome do planeta com a melhor rota.
        optimal_distance:
            Distância do planeta com a melhor rota.
    """
    if can_deliver:
        print(optimal_distance_planet)
        fuel = f"{binary_search(pi, a, b, c, d, optimal_distance):.28f}"
        print(fuel)
    else:
        print("GRAU~~")


def main():
    """Executa o programa principal."""
    getcontext().prec = 36
    pi = recipes_decimal.pi()
    routes_count = int(input())
    while routes_count != 0:
        distances, a, b, c, d = read_data(routes_count)
        max_distance = distance_formula(pi, a, b, c, d, Decimal(50.))
        min_distance = distance_formula(pi, a, b, c, d, Decimal(0.))
        can_deliver, optimal_distance_planet, optimal_distance =\
            print_setter(distances, max_distance, min_distance)
        print_data(can_deliver, pi, a, b, c, d, \
            optimal_distance_planet, optimal_distance)
        routes_count = int(input())


if __name__ == "__main__":
    main()
