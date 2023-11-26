from __future__ import annotations

from abc import ABC
from dataclasses import dataclass


@dataclass
class HtmlElement(ABC):
    parent: HtmlElement | None
    x: int = 0
    y: int = 0

    def compute_screen_position(self) -> tuple[int, int]:
        if not self.parent:
            return (self.x, self.y)
        parent_x, parent_y = self.parent.compute_screen_position()
        return (parent_x + self.x, parent_y + self.y)


@dataclass
class Div(HtmlElement):
    pass

    
@dataclass
class Button(HtmlElement):

    def click(self) -> None:
        print("Click!")


@dataclass
class Span(HtmlElement):
    text: str = ""


def main() -> None:
    root = Div(parent=None, x=25, y=25)
    button = Button(parent=root, x=0, y=0)
    sub_div = Div(parent=root, x=100, y=100)
    span = Span(parent=sub_div, x=40, y=40, text="Hello")
    button.click()
    print(sub_div.compute_screen_position())


if __name__ == "__main__":
    main()
