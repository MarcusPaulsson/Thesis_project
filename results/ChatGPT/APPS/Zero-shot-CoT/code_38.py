def card_game_winner(test_cases):
    results = []
    for case in test_cases:
        n, k1, k2, cards1, cards2 = case
        max_card1 = max(cards1)
        max_card2 = max(cards2)
        if max_card1 > max_card2:
            results.append("YES")
        else:
            results.append("NO")
    return results

# Input reading
t = int(input())
test_cases = []
for _ in range(t):
    n, k1, k2 = map(int, input().split())
    cards1 = list(map(int, input().split()))
    cards2 = list(map(int, input().split()))
    test_cases.append((n, k1, k2, cards1, cards2))

# Get results and print them
results = card_game_winner(test_cases)
for result in results:
    print(result)