from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum, auto
from uuid import UUID, uuid4


class PhoneBrand(Enum):
    APPLE = auto()
    SAMSUNG = auto()
    XIAOMI = auto()
    MOTOROLA = auto()
    LG = auto()
    HUAWEI = auto()
    SONY = auto()


@dataclass
class Adress:
    street: str
    number: int
    city: str
    state: str
    country: str


@dataclass
class Customer:
    name: str
    address: Adress
    email: str


@dataclass
class Phone:
    brand: PhoneBrand
    model: str
    price: float
    serial_number: UUID = field(default_factory=uuid4)


@dataclass
class Plan:
    customer: Customer
    phone: Phone
    start_date: datetime
    contract_length: timedelta
    monthly_price: float
    phone_included: bool = False
