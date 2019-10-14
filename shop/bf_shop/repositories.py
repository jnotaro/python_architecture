import abc
from datetime import datetime
from typing import List, Optional

from bf_shop.entities import Client, Order, Product


class ClientRepository(abc.ABC):
    @abc.abstractmethod
    def create(self, name: str) -> Client:
        pass

    @abc.abstractmethod
    def get(self, client_id: int) -> Client:
        pass


class OrderRepository(abc.ABC):
    @abc.abstractmethod
    def create(self, client: Client) -> Order:
        pass

    @abc.abstractmethod
    def get(self, order_id: int) -> Order:
        pass

    @abc.abstractmethod
    def save(self, order: Order) -> Order:
        pass

    @abc.abstractmethod
    def search(
        self, client: Optional[Client] = None, created: Optional[datetime] = None
    ) -> List[Order]:
        pass


class ProductRepository(abc.ABC):
    @abc.abstractmethod
    def get(self, product_id: int) -> Product:
        pass
