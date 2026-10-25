import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    scores: list[int] = []

    for argument in sys.argv[1:]:
        try:
            scores.append(int(argument))
        except ValueError:
            print(f"Invalid parameter: '{argument}'")

    if not scores:
        print(
            "No scores provided. Usage: "
            "python3 ft_score_analytics.py <score1> <score2> ..."
        )
        return

    total = sum(scores)
    highest = max(scores)
    lowest = min(scores)

    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {total}")
    print(f"Average score: {total / len(scores)}")
    print(f"High score: {highest}")
    print(f"Low score: {lowest}")
    print(f"Score range: {highest - lowest}")


if __name__ == "__main__":
    main()