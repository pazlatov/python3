import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        text = input("Enter new coordinates as floats in format 'x,y,z': ")

        try:
            x_text, y_text, z_text = text.split(",")
        except ValueError:
            print("Invalid syntax: provide exactly three coordinates")
            continue

        values: list[float] = []

        for parameter in (x_text, y_text, z_text):
            try:
                value = float(parameter)
                if not -float("inf") < value < float("inf"):
                    raise ValueError("coordinate must be finite")
                values.append(value)
            except ValueError as error:
                print(f"Error on parameter '{parameter}': {error}")
                break
        else:
            return values[0], values[1], values[2]


def distance(
    first: tuple[float, float, float],
    second: tuple[float, float, float],
) -> float:
    x1, y1, z1 = first
    x2, y2, z2 = second
    return math.sqrt(
        (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2
    )


def main() -> None:
    print("=== Game Coordinate System ===")

    try:
        print("Get a first set of coordinates")
        first = get_player_pos()
        print(f"Got a first tuple: {first}")

        x, y, z = first
        print(f"It includes: X={x}, Y={y}, Z={z}")

        center = (0.0, 0.0, 0.0)
        print(f"Distance to center: {round(distance(first, center), 4)}")

        print("Get a second set of coordinates")
        second = get_player_pos()
        result = round(distance(first, second), 4)
        print(f"Distance between the 2 sets of coordinates: {result}")
    except (EOFError, KeyboardInterrupt):
        print("\nCoordinate input cancelled.")
    except OverflowError:
        print("Coordinates are too large to calculate the distance.")


if __name__ == "__main__":
    main()