from dataclasses import dataclass, field
from datetime import datetime
from typing import List


class Base:
    pass


@dataclass(frozen=True)
class Client(Base):
    id: int
    name: str


@dataclass(frozen=True)
class Product(Base):
    id: int
    name: str
    price: float


@dataclass(frozen=True)
class Order(Base):
    id: int
    created: datetime
    client: Client
    total_cost: float = 0
    items: List[Product] = field(default_factory=list)
