import random


ACHIEVEMENTS = [
    "First Steps",
    "Master Explorer",
    "Treasure Hunter",
    "Boss Slayer",
    "Speed Runner",
    "Survivor",
    "Crafting Genius",
    "World Savior",
    "Collector Supreme",
    "Untouchable",
    "Strategist",
    "Unstoppable",
    "Hidden Path Finder",
    "Sharp Mind",
]


def gen_player_achievements() -> set[str]:
    count = random.randint(7, 10)
    return set(random.sample(ACHIEVEMENTS, count))


def main() -> None:
    print("=== Achievement Tracker System ===")

    players: list[tuple[str, set[str]]] = [
        ("Alice", gen_player_achievements()),
        ("Bob", gen_player_achievements()),
        ("Charlie", gen_player_achievements()),
        ("Dylan", gen_player_achievements()),
    ]

    catalogue = set(ACHIEVEMENTS)
    all_unlocked: set[str] = set()
    common = catalogue.copy()

    for name, achievements in players:
        print(f"Player {name}: {achievements}")
        all_unlocked = all_unlocked.union(achievements)
        common = common.intersection(achievements)

    print(f"\nAll distinct achievements: {all_unlocked}")
    print(f"Common achievements: {common}")

    for name, achievements in players:
        others: set[str] = set()

        for other_name, other_achievements in players:
            if other_name != name:
                others = others.union(other_achievements)

        exclusive = achievements.difference(others)
        print(f"Only {name} has: {exclusive}")

    for name, achievements in players:
        missing = catalogue.difference(achievements)
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    main()