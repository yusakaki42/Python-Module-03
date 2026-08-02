#!/usr/bin/env python3

import sys

def perse_inventory(args: list) -> dict[str, int]:
    inventory: dict[str, int] = {}

    for arg in args:
        parts = arg.split(':')
        print(f"Error - invalid parameter '{arg}'")



def main() -> None:
    print("=== Inventory System Analysis ===")

    if len(sys.argv) == 1:
        print("At the beginning of the game, your inventory is usually empty ;)")
        return

    inventroy = parse_inventory(sys.argv[1:])





main()
