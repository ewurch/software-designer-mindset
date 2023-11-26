from typing import Callable

IntFunction = Callable[[int], int]


class Book:
    def __init__(self, author: str, title: str, pages: int) -> None:
        self.author = author
        self.title = title
        self.pages = pages

    def __len__(self) -> int:
        return self.pages


def main():
    my_str = "Hello, World!"
    print(len(my_str))
    my_list = [1, 2, 3, 4, 5]
    print(len(my_list))
    my_dict = {"a": 1, "b": 2, "c": 3}
    print(len(my_dict))
    my_book = Book("John Doe", "My Book", 300)
    print(len(my_book))


if __name__ == "__main__":
    main()
