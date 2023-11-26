from abc import ABC
from dataclasses import dataclass
from datetime import datetime
from time import time

# each social channel has a type
# and the current number of followers
@dataclass
class SocialChannel(ABC):
    type: str
    followers: int
    
    def post(self, message: str) -> None:
        print(f"{self.type} channel: {message}")
    

# each post has a message and the timestamp when it should be posted
@dataclass
class Post:
    message: str
    timestamp: float


def process_schedule(posts: list[Post], channels: list[SocialChannel]) -> None:
    for post in posts:
        for channel in channels:
            if post.timestamp <= time():
                channel.post(post.message)


def main() -> None:
    posts = [
        Post(
            "Grandma's carrot cake is available again (limited quantities!)!",
            1568123400,
        ),
        Post("Get your carrot cake now, the promotion ends today!", 1568133400),
    ]
    channels = [
        SocialChannel("youtube", 100),
        SocialChannel("facebook", 100),
        SocialChannel("twitter", 100),
    ]
    process_schedule(posts, channels)


if __name__ == "__main__":
    main()
