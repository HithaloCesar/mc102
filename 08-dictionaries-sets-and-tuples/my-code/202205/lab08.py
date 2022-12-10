from typing import Dict, Set
from datetime import datetime, timedelta


class Product():
    def __init__(
            self, quantity: int, category: str,
            price: float, expiration_date: datetime) -> None:
        """Cria ou atualiza um produto.

        Args:
            quantity: Quantidade do produto a ser adicionada.
            category: Categoria do produto.
            price: Preço do produto.
            expiration_date: Data de validade do produto.

        """
        self.quantity = quantity
        self.category = category
        self.price = price
        self.expiration_date = expiration_date

    def subtract(self, subtrahend: int) -> str:
        """Subtrai do estoque uma quantidade de um determinado produto.

        Args:
            subtrahend: Quantidade que deve ser subtraída.

        Returns:
            Feedback da operação.
        """
        if self.quantity >= subtrahend:
            self.quantity -= subtrahend
            return "SUCCESS"
        return "ERROR"


def stock_mode(products: Dict[str, Product], resupply: Set[str]) -> None:
    """Entra no modo de estoque.

    Args:
        products: Cada chave é um nome de produto e cada valor é uma instância
            da classe Product.
        resupply: Nomes dos produtos que devem ser reabastecidos.

    """
    operations = int(input())
    for _ in range(operations):
        entry = input().split()
        mode = entry[0]
        name = entry[1]
        quantity = int(entry[2])
        if mode == "0":
            category = entry[3]
            price = float(entry[4])
            expiration_date = datetime.strptime(entry[5], "%d%m%Y")
            add_update_product(
                products, name, quantity, category,
                price, expiration_date, resupply
            )
        elif mode == "1":
            remove_product(products, name, quantity)


def add_update_product(
        products: Dict[str, Product], name: str, quantity: int, category: str,
        price: float, expiration_date: datetime, resupply: Set[str]) -> None:
    """Adiciona ou atualiza um produto no estoque.

    Args:
        products: Cada chave é o nome do produto e cada valor é uma instância
            da classe Product.
        name: Nome do produto.
        quantity: Quantidade do produto a ser adicionada.
        category: Categoria do produto.
        price: Preço do produto.
        expiration_date: Data de validade do produto.
        resupply: Nomes dos produtos que devem ser reabastecidos.

    """
    products[name] = Product(quantity, category, price, expiration_date)
    resupply.discard(name)


def remove_product(
        products: Dict[str, Product], name: str,
        quantity: int) -> None:
    """Remove do estoque uma quantidade de um produto.

    Args:
        products: Cada chave é o nome do produto e cada valor é uma instância
            da classe Product.
        name: Nome do produto.
        quantity: Quantidade do produto a ser removida.

    """
    try:
        feedback = products[name].subtract(quantity)
        if products[name].quantity == 0:
            del products[name]
    except KeyError:
        feedback = "ERROR"
    print(feedback)


def store_mode(
        balance: float, products: Dict[str, Product],
        resupply: Set[str]) -> float:
    """Entra no modo de loja.

    Args:
        balance: Saldo do dia.
        products: Cada chave é o nome do produto e cada valor é uma instância
            da classe Product.
        resupply: Nomes dos produtos que devem ser reabastecidos.

    Returns:
        Saldo do dia.

    """
    operations = int(input())
    for _ in range(operations):
        name, quantity_sold = input().split()
        quantity_sold = int(quantity_sold)
        balance = sell_product(
            products, name, quantity_sold, balance, resupply
        )
    return balance


def sell_product(
        products: Dict[str, Product], name: str, quantity_sold: int,
        balance: float, resupply: Set[str]) -> float:
    """Vende uma quantidade de um produto.

    Caso o produto já não exista no dicionário de produtos, ignora a operação.

    Args:
        products: Cada chave é o nome do produto e cada valor é uma instância
            da classe Product.
        name: Nome do produto.
        quantity_sold: Quantidade do produto a ser vendida.
        balance: Saldo do dia.
        resupply: Nomes dos produtos que devem ser reabastecidos.

    Returns:
        Saldo do dia.

    """
    try:
        products[name].quantity -= quantity_sold
        balance += products[name].price * quantity_sold
        if products[name].quantity == 0:
            del products[name]
            resupply.add(name)
    except KeyError:
        pass
    return balance


def report(
        products: Dict[str, Product], resupply: Set[str],
        balance: float) -> None:
    """Imprime o relatório do dia.

    Args:
        products: Cada chave é o nome do produto e cada valor é uma instância
            da classe Product.
        balance: Saldo do dia.
        resupply: Nomes dos produtos que devem ser reabastecidos.

    """
    current_date = datetime.strptime(input(), "%d%m%Y")
    stock_report(products)
    print("* SALDO", "{:.2f}".format(balance))
    resupply_report(resupply)
    sale_report(products, current_date)


def stock_report(products: Dict[str, Product]) -> None:
    """Imprime o nome de cada produto presente no estoque e sua quantidade.

    Args:
        products: Cada chave é o nome do produto e cada valor é uma instância
            da classe Product.

    """
    print("* ESTOQUE")
    categories_set = set()
    for product in products.values():
        categories_set.add(product.category)
    for category in sorted(list(categories_set)):
        print("-", category)
        for name, product in sorted(products.items()):
            if product.category == category:
                print(name, product.quantity)


def resupply_report(resupply: Set[str]) -> None:
    """Imprime o nome de cada produto que deve ser reabastecido no estoque.

    Args:
        resupply: Nomes dos produtos que devem ser reabastecidos.

    """
    if resupply != set():
        print("* REPOSICAO")
        for product in sorted(resupply):
            print(product)


def sale_report(products: Dict[str, Product], current_date: datetime) -> None:
    """Imprime os produtos que devem entrar em promoção no dia seguinte.

    Args:
        products: Cada chave é o nome do produto e cada valor é uma instância
            da classe Product.
        current_date: Data atual, no formato DDMMYYYY.

    """
    title_printed = False
    for name, product in sorted(products.items()):
        if current_date + timedelta(days=7) >= product.expiration_date:
            if not title_printed:
                print("* PROMOCAO")
                title_printed = True
            print(name)


def main():
    """Executa o programa principal."""
    products = {}
    resupply = set()
    balance = 0
    mode = None
    while mode != "0":
        mode = input()
        if mode == "1":
            stock_mode(products, resupply)
        elif mode == "2":
            balance = store_mode(balance, products, resupply)
        elif mode == "0":
            report(products, resupply, balance)


if __name__ == "__main__":
    main()
