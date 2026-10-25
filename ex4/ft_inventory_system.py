import sys


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}

    for argument in sys.argv[1:]:
        parts = argument.split(":")

        if len(parts) != 2 or not parts[0].strip():
            print(f"Error - invalid parameter '{argument}'")
            continue

        name = parts[0].strip()

        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue

        try:
            quantity = int(parts[1])
            if quantity < 0:
                raise ValueError("quantity cannot be negative")
        except ValueError as error:
            print(f"Quantity error for '{name}': {error}")
            continue

        inventory[name] = quantity

    print(f"Got inventory: {inventory}")

    items = list(inventory.keys())
    print(f"Item list: {items}")

    total = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total}")

    for name in inventory:
        percentage = 0.0
        if total:
            percentage = round(inventory[name] / total * 100, 1)
        print(f"Item {name} represents {percentage}%")

    if items:
        most = items[0]
        least = items[0]

        for name in inventory:
            if inventory[name] > inventory[most]:
                most = name
            if inventory[name] < inventory[least]:
                least = name

        print(f"Item most abundant: {most} with quantity {inventory[most]}")
        print(f"Item least abundant: {least} with quantity {inventory[least]}")
    else:
        print("Inventory is empty; no most or least abundant item.")

    new_item = "magic_item"
    while new_item in inventory:
        new_item += "_new"

    inventory.update({new_item: 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()