import random
import string
from datetime import datetime


def generate_id(
    length: int, uppercase: str = string.ascii_uppercase, digits: str = string.digits
) -> str:
    return "".join(random.choice(uppercase + digits) for _ in range(length))


def weekday(today: datetime = datetime.today()) -> str:
    return f"{today:%A}"


def main() -> None:
    print(f"Today is a {weekday()}")
    print(f"Your id = {generate_id(10)}")


if __name__ == "__main__":
    main()
