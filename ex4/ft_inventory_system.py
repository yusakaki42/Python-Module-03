#!/usr/bin/env python3

import sys


def parse_inventory(args: list) -> dict[str, int]:
    inventory: dict[str, int] = {}

    for arg in args:
        parts = arg.split(':')
        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue

        name = parts[0]
        quantity_str = parts[1]

        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue

        try:
            quantity = int(quantity_str)
        except ValueError as e:
            print(f"Quantity error for '{name}': {e}")
            continue

        inventory[name] = quantity

    return inventory


def print_stats(inventory: dict[str, int]) -> None:
    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")

    total = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total}")

    for name, qty in inventory.items():
        percentage = round(qty / total * 100, 1)
        print(f"Item sword represents {percentage}%")

    most_item = item_list[0]
    most_qty = inventory[most_item]

    least_item = item_list[0]
    least_qty = inventory[least_item]

    for item, qty in inventory.items():
        if qty > most_qty:
            most_qty = qty
            most_item = item
        if qty < least_qty:
            least_qty = qty
            least_item = item

    print(f"Item most abundant: {most_item} with quantity {most_qty}")
    print(f"Item least abundant: {least_item} with quantity {least_qty}")


def main() -> None:
    print("=== Inventory System Analysis ===")

    if len(sys.argv) == 1:
        print(
            "Usage: python3 ft_inventory_system.py "
            "<item1:quantity1> <item2:quantity2> ..."
        )
        return

    inventory = parse_inventory(sys.argv[1:])

    if len(inventory) == 0:
        print(
            "Usage: python3 ft_inventory_system.py "
            "<item1:quantity1> <item2:quantity2> ..."
        )
        return

    print(f"Got inventory: {inventory}")

    print_stats(inventory)

    inventory.update({'magic_item': 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
