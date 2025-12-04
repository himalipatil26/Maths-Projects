#!/usr/bin/env python3
"""
Probability Simulator
- Coin toss
- Dice roll
- Card draw

Shows experimental vs theoretical probabilities and (optionally) plots results.

Usage: run the script and follow the menu. Requires Python 3.8+.
Optional: install matplotlib to see plots: pip install matplotlib

Author: ChatGPT
"""

import random
import math
import sys
from collections import Counter

try:
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except Exception:
    HAS_MATPLOTLIB = False


def clear():
    print("\n" * 2)


# --------------------- Utilities ---------------------

def ask_int(prompt, default=None, minval=None, maxval=None):
    while True:
        raw = input(f"{prompt}" + (f" [{default}]" if default is not None else "") + ": ")
        if raw.strip() == "" and default is not None:
            return default
        try:
            v = int(raw)
            if minval is not None and v < minval:
                print("Value too small")
                continue
            if maxval is not None and v > maxval:
                print("Value too large")
                continue
            return v
        except ValueError:
            print("Please enter an integer.")


def proportion_table(counter, total):
    rows = []
    for k in sorted(counter.keys(), key=lambda x: (str(x))):
        cnt = counter[k]
        rows.append((k, cnt, cnt/total))
    return rows


# --------------------- Coin ---------------------

def theoretical_coin():
    return {"Heads": 0.5, "Tails": 0.5}


def simulate_coin(trials=1000, biased_p_heads=None):
    """Return Counter of results"""
    results = Counter()
    for _ in range(trials):
        r = random.random()
        p = biased_p_heads if biased_p_heads is not None else 0.5
        results["Heads" if r < p else "Tails"] += 1
    return results


# --------------------- Dice ---------------------

def theoretical_dice(sides=6):
    return {i: 1/sides for i in range(1, sides+1)}


def simulate_dice(trials=1000, sides=6):
    results = Counter()
    for _ in range(trials):
        roll = random.randint(1, sides)
        results[roll] += 1
    return results


# --------------------- Cards ---------------------
RANKS = [str(n) for n in range(2, 11)] + ["J", "Q", "K", "A"]
SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
DECK = [f"{r} of {s}" for s in SUITS for r in RANKS]


def theoretical_card_single():
    # single draw theoretical probabilities for rank and suit
    rank_prob = {r: 4/52 for r in RANKS}
    suit_prob = {s: 13/52 for s in SUITS}
    specific_card_prob = 1/52
    return {"rank": rank_prob, "suit": suit_prob, "specific": specific_card_prob}


def comb(n, k):
    return math.comb(n, k)


def theoretical_two_card_pair():
    # probability that two cards drawn without replacement have the same rank
    # choose rank (13 ways), choose 2 from 4 of that rank / choose any 2 from 52
    return (13 * comb(4, 2)) / comb(52, 2)


def theoretical_two_aces():
    # both cards are aces
    return comb(4, 2) / comb(52, 2)


def simulate_cards(trials=1000, draw_count=1):
    # returns counters for ranks & suits and also some special events for draw_count==2
    rank_counter = Counter()
    suit_counter = Counter()
    specific_counter = Counter()
    pair_count = 0
    both_aces = 0

    for _ in range(trials):
        deck = DECK.copy()
        random.shuffle(deck)
        draw = deck[:draw_count]
        # single-card metrics
        for card in draw:
            rank, _, suit = card.partition(' of ')
            rank_counter[rank] += 1
            suit_counter[suit] += 1
            specific_counter[card] += 1

        if draw_count == 2:
            ranks = [c.split(' of ')[0] for c in draw]
            if ranks[0] == ranks[1]:
                pair_count += 1
            if all(r == 'A' for r in ranks):
                both_aces += 1

    return {
        'rank': rank_counter,
        'suit': suit_counter,
        'specific': specific_counter,
        'pair_count': pair_count,
        'both_aces': both_aces,
    }


# --------------------- Display & Plot helpers ---------------------

def print_results(counter, total, title="Results"):
    print(f"--- {title} (total={total}) ---")
    rows = proportion_table(counter, total)
    for k, cnt, prop in rows:
        print(f"{str(k):>12} : {cnt:>6}  ({prop:.4f})")
    print()


def plot_counter(counter, total, title=""):
    if not HAS_MATPLOTLIB:
        print("matplotlib not available. Skipping plot.")
        return
    labels = list(sorted(counter.keys(), key=lambda x: str(x)))
    values = [counter[k] for k in labels]
    plt.figure(figsize=(8,4))
    plt.bar(range(len(labels)), values)
    plt.xticks(range(len(labels)), labels, rotation=45, ha='right')
    plt.title(title + f" (n={total})")
    plt.tight_layout()
    plt.show()


# --------------------- Interactive Menu ---------------------

def run_coin_menu():
    trials = ask_int("Number of trials", default=1000, minval=1)
    bias = input("Probability of heads? (press Enter for fair coin 0.5) ")
    p = None
    if bias.strip() != "":
        try:
            p = float(bias)
            if not (0 <= p <= 1):
                print("Invalid probability, using fair coin.")
                p = None
        except Exception:
            print("Couldn't parse probability, using fair coin.")
            p = None
    exp = simulate_coin(trials, biased_p_heads=p)
    theo = theoretical_coin()
    print_results(exp, trials, title="Coin toss (experimental)")
    print("--- Theoretical ---")
    for k, v in theo.items():
        print(f"{k:>6} : {v:.4f}")
    if input("Plot? (y/N) ").lower().startswith('y'):
        plot_counter(exp, trials, "Coin toss")


def run_dice_menu():
    sides = ask_int("Number of sides on die", default=6, minval=2)
    trials = ask_int("Number of trials", default=1000, minval=1)
    exp = simulate_dice(trials, sides)
    theo = theoretical_dice(sides)
    print_results(exp, trials, title=f"{sides}-sided die (experimental)")
    print("--- Theoretical ---")
    for k in sorted(theo.keys()):
        print(f"{k:>2} : {theo[k]:.4f}")
    if input("Plot? (y/N) ").lower().startswith('y'):
        plot_counter(exp, trials, f"{sides}-sided die")


def run_card_menu():
    print("Standard 52-card deck. Ranks:", ','.join(RANKS))
    draw_count = ask_int("How many cards to draw per trial? (1 or 2)", default=1, minval=1, maxval=2)
    trials = ask_int("Number of trials", default=1000, minval=1)
    exp = simulate_cards(trials, draw_count)

    print_results(exp['rank'], trials * draw_count, title="Rank frequencies (experimental)")
    print_results(exp['suit'], trials * draw_count, title="Suit frequencies (experimental)")

    theo_single = theoretical_card_single()
    print("--- Theoretical (single draw) ---")
    print("Rank (each):", next(iter(theo_single['rank'].items()))[1])
    print("Suit (each):", next(iter(theo_single['suit'].items()))[1])
    print("Specific card:", theo_single['specific'])

    if draw_count == 2:
        pair_freq = exp['pair_count'] / trials
        both_aces_freq = exp['both_aces'] / trials
        print(f"Experimental: Two-card same-rank fraction: {pair_freq:.6f}")
        print(f"Theoretical two-card same-rank: {theoretical_two_card_pair():.6f}")
        print(f"Experimental: Both aces fraction: {both_aces_freq:.6f}")
        print(f"Theoretical both aces: {theoretical_two_aces():.6f}")

    if input("Plot rank frequencies? (y/N) ").lower().startswith('y'):
        plot_counter(exp['rank'], trials * draw_count, "Card rank frequencies")


def main_menu():
    random.seed()
    while True:
        print("\nProbability Simulator")
        print("1) Coin toss")
        print("2) Dice roll")
        print("3) Card draw")
        print("4) Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            run_coin_menu()
        elif choice == '2':
            run_dice_menu()
        elif choice == '3':
            run_card_menu()
        elif choice == '4':
            print("Bye")
            sys.exit(0)
        else:
            print("Invalid option")


if __name__ == '__main__':
    main_menu()
