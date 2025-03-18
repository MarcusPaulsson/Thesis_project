import random

def calculate_hand_value(hand):
    """Calculates the value of a hand in Blackjack. Aces can be 1 or 11."""
    ace_count = hand.count('A')
    total = 0
    for card in hand:
        if card.isdigit():
            total += int(card)
        elif card in ('J', 'Q', 'K'):
            total += 10
        elif card == 'A':
            total += 11
    while total > 21 and ace_count > 0:
        total -= 10
        ace_count -= 1
    return total

def deal_card(deck):
    """Deals a card from the deck."""
    return deck.pop()

def create_deck():
    """Creates a standard 52-card deck."""
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [rank for suit in suits for rank in ranks] * 4 # Use 4 decks
    random.shuffle(deck)
    return deck

def display_hand(hand, hidden=False):
    """Displays a hand of cards."""
    if hidden:
        print("[Hidden Card]", end=" ")
        for card in hand[1:]:
            print(card, end=" ")
    else:
        for card in hand:
            print(card, end=" ")
    print()

def play_blackjack():
    """Plays a game of Blackjack."""
    deck = create_deck()
    player_hand = []
    dealer_hand = []

    # Deal initial hands
    for _ in range(2):
        player_hand.append(deal_card(deck))
        dealer_hand.append(deal_card(deck))

    print("Dealer's hand:")
    display_hand(dealer_hand, hidden=True)
    print("Your hand:")
    display_hand(player_hand)
    player_value = calculate_hand_value(player_hand)
    print(f"Your hand value: {player_value}")

    # Player's turn
    while player_value < 21:
        action = input("Hit or stand? (h/s): ").lower()
        if action == 'h':
            player_hand.append(deal_card(deck))
            print("Your hand:")
            display_hand(player_hand)
            player_value = calculate_hand_value(player_hand)
            print(f"Your hand value: {player_value}")
            if player_value > 21:
                print("You bust!")
                return "dealer"
        elif action == 's':
            break
        else:
            print("Invalid action. Please enter 'h' or 's'.")

    # Dealer's turn
    print("\nDealer's hand:")
    display_hand(dealer_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    print(f"Dealer's hand value: {dealer_value}")

    if player_value > 21:
        return "dealer"

    while dealer_value < 17:  # Dealer hits on 16 or less
        print("Dealer hits.")
        dealer_hand.append(deal_card(deck))
        display_hand(dealer_hand)
        dealer_value = calculate_hand_value(dealer_hand)
        print(f"Dealer's hand value: {dealer_value}")
        if dealer_value > 21:
            print("Dealer busts!")
            return "player"

    # Determine the winner
    print("\nFinal hands:")
    print("Your hand:", end=" ")
    display_hand(player_hand)
    print("Dealer's hand:", end=" ")
    display_hand(dealer_hand)

    if dealer_value > 21:
        return "player"
    elif player_value > dealer_value or dealer_value > 21:
        return "player"
    elif player_value == dealer_value:
        return "push"
    else:
        return "dealer"

if __name__ == "__main__":
    while True:
        print("\nLet's play Blackjack!")
        winner = play_blackjack()

        if winner == "player":
            print("You win!")
        elif winner == "dealer":
            print("Dealer wins!")
        else:
            print("It's a push (tie)!")

        play_again = input("Play again? (y/n): ").lower()
        if play_again != 'y':
            break
    print("Thanks for playing!")