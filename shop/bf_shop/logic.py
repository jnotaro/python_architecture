from dataclasses import replace
from typing import List

from injector import inject

from bf_shop.entities import Order
from bf_shop.repositories import ClientRepository, OrderRepository, ProductRepository


class OrderLogic:
    @inject
    def __init__(
        self,
        orders: OrderRepository,
        products: ProductRepository,
        clients: ClientRepository,
    ) -> None:
        self._orders: OrderRepository = orders
        self._products: ProductRepository = products
        self._clients: ClientRepository = clients

    def search(self, client_id: int) -> List[Order]:
        client = self._clients.get(client_id)
        return self._orders.search(client)

    def create(self, client_id: int) -> Order:
        client = self._clients.get(client_id)
        return self._orders.create(client=client)

    def add_product(self, order_id: int, product_id: int) -> Order:
        order = self._orders.get(order_id)
        product = self._products.get(product_id)

        order = replace(
            order,
            items=order.items + [product],
            total_cost=order.total_cost + product.price,
        )

        return self._orders.save(order)
