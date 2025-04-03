t = int(input())
for _ in range(t):
    n, k1, k2 = map(int, input().split())
    player1_cards = list(map(int, input().split()))
    player2_cards = list(map(int, input().split()))
    
    # The winner will be the player with the highest card
    highest_card_player1 = max(player1_cards)
    highest_card_player2 = max(player2_cards)
    
    if highest_card_player1 > highest_card_player2:
        print("YES")
    else:
        print("NO")