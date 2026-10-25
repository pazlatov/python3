import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = [
        "run", "eat", "sleep", "grab", "move",
        "climb", "swim", "release", "use",
    ]

    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield name, action


def consume_event(
    events: list[tuple[str, str]],
) -> Generator[tuple[str, str], None, None]:
    while events:
        index = random.randrange(len(events))
        yield events.pop(index)


def main() -> None:
    print("=== Game Data Stream Processor ===")
    stream = gen_event()

    for number in range(1000):
        name, action = next(stream)
        print(f"Event {number}: Player {name} did action {action}")

    events: list[tuple[str, str]] = []
    for _ in range(10):
        events.append(next(stream))

    print(f"\nBuilt list of 10 events: {events}")

    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    main()