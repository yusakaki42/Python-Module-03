#! /usr/bin/env python3


import random


ALL_ACHIEVEMENTS = [
    'First Steps', 'Speed Runner', 'Boss Slayer', 'Treasure Hunter',
    'Survivor', 'Strategist', 'Unstoppable', 'Untouchable',
    'Master Explorer', 'Sharp Mind', 'Crafting Genius', 'World Savior',
    'Collector Supreme', 'Hidden Path Finder', 'Dragon Slayer',
    'Night Owl', 'Pacifist', 'Completionist'
]


def gen_player_achievements() -> set[str]:
    count = random.randint(3, 10)
    picks = random.sample(ALL_ACHIEVEMENTS, count)
    return set(picks)


def main() -> None:
    print("=== Achievement Tracker System ===")
    print()
    players = {
        'Alice': gen_player_achievements(),
        'Bob': gen_player_achievements(),
        'Charlie': gen_player_achievements(),
        'Dylan': gen_player_achievements(),
    }

    for name, achievements in players.items():
        print(f"Player {name}: {achievements}")
    print()

    all_achievements: set[str] = set()
    for achievements in players.values():
        all_achievements = set.union(all_achievements, achievements)
    print(f"All distinct achievements: {all_achievements}")
    print()

    common_achievements: set[str] = set(ALL_ACHIEVEMENTS)
    for achievements in players.values():
        common_achievements = set.intersection(
            common_achievements, achievements)
    print(f"Common achievements: {common_achievements}")
    print()

    for name, achievements in players.items():
        others: set[str] = set()
        for other_name, other_ach in players.items():
            if other_name != name:
                others = set.union(others, other_ach)
        unique = set.difference(achievements, others)
        print(f"Only {name} has: {unique}")
    print()

    full_set = set(ALL_ACHIEVEMENTS)
    for name, achievements in players.items():
        missing = set.difference(full_set, achievements)
        print(f"{name} is missing: {missing}")


main()
