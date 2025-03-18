import random

# Card values
VALUES = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

# Card deck
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = list(VALUES.keys())
DECK = [(rank, suit) for rank in RANKS for suit in SUITS]

def calculate_hand_value(hand):
    value = sum(VALUES[card[0]] for card in hand)
    # Adjust for Aces
    aces = sum(1 for card in hand if card[0] == 'A')
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def deal_card(deck):
    return deck.pop(random.randint(0, len(deck) - 1))

def display_hand(hand, hide_first_card=False):
    if hide_first_card:
        return "[Hidden Card], " + ", ".join(f"{rank} of {suit}" for rank, suit in hand[1:])
    return ", ".join(f"{rank} of {suit}" for rank, suit in hand)

def blackjack():
    print("Welcome to Blackjack!")
    deck = DECK.copy()
    random.shuffle(deck)

    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]

    # Player's turn
    while True:
        print(f"Your hand: {display_hand(player_hand)} (Value: {calculate_hand_value(player_hand)})")
        print(f"Dealer's hand: {display_hand(dealer_hand, hide_first_card=True)}")
        
        if calculate_hand_value(player_hand) == 21:
            print("Blackjack! You win!")
            return
        elif calculate_hand_value(player_hand) > 21:
            print("Bust! You lose.")
            return

        action = input("Do you want to (h)it or (s)tand? ").strip().lower()
        if action == 'h':
            player_hand.append(deal_card(deck))
        elif action == 's':
            break

    # Dealer's turn
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck))

    # Final results
    print(f"Your hand: {display_hand(player_hand)} (Value: {calculate_hand_value(player_hand)})")
    print(f"Dealer's hand: {display_hand(dealer_hand)} (Value: {calculate_hand_value(dealer_hand)})")

    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    if dealer_value > 21 or player_value > dealer_value:
        print("You win!")
    elif player_value < dealer_value:
        print("You lose.")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    blackjack()