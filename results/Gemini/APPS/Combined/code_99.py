def solve():
    n = int(input())
    a1, a2, a3 = map(int, input().split())
    b1, b2, b3 = map(int, input().split())

    # Calculate minimum wins
    min_wins = 0
    
    # Calculate maximum wins
    max_wins = min(a1, b2) + min(a2, b3) + min(a3, b1)

    # Calculate minimum losses for Bob, which translates to maximum draws and minimum wins for Alice
    min_loss_bob_rock = min(a1, b1)
    min_loss_bob_scissors = min(a2, b2)
    min_loss_bob_paper = min(a3, b3)

    remaining_a1 = a1 - min_loss_bob_rock
    remaining_a2 = a2 - min_loss_bob_scissors
    remaining_a3 = a3 - min_loss_bob_paper

    remaining_b1 = b1 - min_loss_bob_rock
    remaining_b2 = b2 - min_loss_bob_scissors
    remaining_b3 = b3 - min_loss_bob_paper

    min_wins = max(0, remaining_a1 - (remaining_b1 + remaining_b3), remaining_a2 - (remaining_b2 + remaining_b1), remaining_a3 - (remaining_b3 + remaining_b2))

    print(min_wins, max_wins)

solve()