def calculate_wins():
    n = int(input("Enter the total number of games: "))
    a1, a2, a3 = map(int, input("Enter Alice's counts (a1 a2 a3): ").split())
    b1, b2, b3 = map(int, input("Enter Bob's counts (b1 b2 b3): ").split())

    # Maximum wins for Alice
    max_wins = min(a1, b3) + min(a2, b1) + min(a3, b2)

    # Minimum wins for Alice
    bob_wins = min(b1, a2) + min(b2, a3) + min(b3, a1)
    min_wins = n - bob_wins

    print(min_wins, max_wins)

if __name__ == "__main__":
    calculate_wins()