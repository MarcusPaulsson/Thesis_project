def card_game_winner(test_cases):
    results = []
    for case in test_cases:
        n, k1, k2, player1_cards, player2_cards = case
        max_card_player1 = max(player1_cards)
        max_card_player2 = max(player2_cards)
        if max_card_player1 > max_card_player2:
            results.append("YES")
        else:
            results.append("NO")
    return results

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n, k1, k2 = map(int, input().split())
    player1_cards = list(map(int, input().split()))
    player2_cards = list(map(int, input().split()))
    test_cases.append((n, k1, k2, player1_cards, player2_cards))

# Get results
results = card_game_winner(test_cases)

# Print results
for result in results:
    print(result)