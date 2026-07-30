#!/usr/bin/env python3

import sys


def main() -> None:
    args = sys.argv
    print("=== Command Quest ===")
    print(f"Program name: {args[0]}")

    if len(args) == 1:
        print("No arguments provided!")
    else:
        print("Program name: {args[0]}")
        for i, arg in enumerate(args[1:], start=1):
            print("Argument {i}: {arg}")


    print("Total arguments: {len(args)}")


main()
