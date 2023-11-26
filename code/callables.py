from dataclasses import dataclass
from functools import partial
from typing import Callable


@dataclass
class Customer:
    name: str
    age: int


def send_email_promotion(
    customers: list[Customer], is_eligible: Callable[[Customer], bool]
) -> None:
    for customer in customers:
        if is_eligible(customer):
            print(f"Sending email promotion to {customer.name}")


def is_eligible_for_promotion(customer: Customer, cutoff_age: int = 50) -> bool:
    return customer.age >= cutoff_age


def main() -> None:
    customers = [
        Customer("John Doe", 17),
        Customer("Jane Doe", 19),
        Customer("Dave Smith", 20),
        Customer("Tom Jones", 16),
        Customer("Mary Smith", 17),
    ]
    is_eligible = partial(is_eligible_for_promotion, cutoff_age=12)
    send_email_promotion(customers, is_eligible)


main()
