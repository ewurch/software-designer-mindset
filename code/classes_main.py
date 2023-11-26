import math
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Vehicle(ABC):
    @abstractmethod
    def reserve(self, start: datetime, length: int):
        print(f"Vehicle reserved from {start} for {length} days")


@dataclass
class Car(Vehicle):
    model: str
    reserved: bool = False

    def reserve(self, start: datetime, length: int):
        self.reserved = True
        print(f"Car {self.model} reserved from {start} for {length} days")


@dataclass
class Truck(Vehicle):
    model: str
    reserved: bool = False
    reserved_trailer: bool = False

    def reserve(self, start: datetime, length: int):
        months = math.ceil(length / 30)
        self.reserved = True
        print(
            f"Truck {self.model} and Trailer={self.reserved_trailer} reserved from {start} for {months} months"
        )


def reserve_now(vehicle: Vehicle):
    vehicle.reserve(datetime.now(), 40)


def main() -> None:
    car = Car("BMW")
    truck = Truck("Volvo")
    reserve_now(car)
    reserve_now(truck)


if __name__ == "__main__":
    main()
