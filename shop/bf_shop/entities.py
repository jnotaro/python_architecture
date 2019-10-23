from dataclasses import dataclass, field
from datetime import datetime
from typing import List

@dataclass(frozen=True)
class BaseEntity:
    id: int
    created: datetime

@dataclass(frozen=True)
class Client(BaseEntity):
    name: str


@dataclass(frozen=True)
class Product(BaseEntity):
    name: str
    price: float


@dataclass(frozen=True)
class Order(BaseEntity):
    client: Client
    total_cost: float = 0
    items: List[Product] = field(default_factory=list)
