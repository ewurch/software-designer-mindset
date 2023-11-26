import math
from dataclasses import dataclass
from datetime import datetime
from typing import Protocol


class Vehicle(Protocol):
    def reserve(self, start: datetime, length: int):
        ...


class LicenseHolder(Protocol):
    def renew_license(self, new_licese_date: datetime):
        ...

@dataclass
class Car:
    model: str
    reserved: bool = False

    def reserve(self, start: datetime, length: int):
        self.reserved = True
        print(f"Car {self.model} reserved from {start} for {length} days")


@dataclass
class Truck:
    model: str
    reserved: bool = False
    reserved_trailer: bool = False

    def reserve(self, start: datetime, length: int):
        months = math.ceil(length / 30)
        self.reserved = True
        print(
            f"Truck {self.model} and Trailer={self.reserved_trailer} reserved from {start} for {months} months"
        )
        
    def renew_license(self, new_license_date: datetime):
        print("License renewed: ", new_license_date)


def reserve_now(vehicle: Vehicle):
    vehicle.reserve(datetime.now(), 40)

def renew_license_now(license_holder: LicenseHolder):
    license_holder.renew_license(datetime.now())

def main() -> None:
    car = Car("BMW")
    truck = Truck("Volvo")
    reserve_now(car)
    reserve_now(truck)
    renew_license_now(truck)


if __name__ == "__main__":
    main()
