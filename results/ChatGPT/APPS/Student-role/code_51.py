def can_have_no_winner(n, k, d1, d2):
    # Remaining games
    remaining_games = n - k
    
    # Wins of team 1, 2, and 3
    w1 = (d1 + d2) // 2
    w2 = (d1 - d2) // 2
    w3 = (d2 - d1) // 2

    # Check if the calculated wins are valid
    if (d1 + d2) % 2 != 0 or w1 < 0 or w2 < 0 or w3 < 0:
        return "no"
    
    # Total wins after k games
    total_wins = w1 + w2 + w3
    
    # Remaining games should be enough to balance the wins
    if total_wins + remaining_games >= 0 and (total_wins + remaining_games) % 3 == 0:
        return "yes"
    
    return "no"

t = int(input())
for _ in range(t):
    n, k, d1, d2 = map(int, input().split())
    print(can_have_no_winner(n, k, d1, d2))