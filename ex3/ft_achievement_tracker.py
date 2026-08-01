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
        print(f"Player {name}: {{achievements}}")
