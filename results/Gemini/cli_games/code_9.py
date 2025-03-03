import random

def calculate_hand_value(hand):
    """Calculates the value of a hand in Blackjack.

    Args:
        hand: A list of strings representing the cards in the hand.
              Each string is the card's rank (e.g., 'A', 'K', '10', '2').

    Returns:
        The integer value of the hand.  Handles Aces correctly.
    """
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
    """Deals a card from the deck.

    Args:
        deck: A list of strings representing the deck of cards.

    Returns:
        A tuple containing:
            - The card dealt (string).
            - The updated deck (list).
    """
    card = deck.pop()
    return card, deck


def create_deck():
    """Creates a standard 52-card deck.

    Returns:
        A list of strings representing the deck of cards, shuffled.
    """
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [rank for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck


def display_hand(hand, is_dealer=False, hide_first_card=False):
    """Displays a hand of cards.

    Args:
        hand: A list of strings representing the cards in the hand.
        is_dealer: Boolean, True if the hand is the dealer's.
        hide_first_card: Boolean, True if the dealer's first card should be hidden.
    """
    if is_dealer and hide_first_card:
        print("Dealer's Hand: [Hidden],", ', '.join(hand[1:]))
    else:
        print("Dealer's Hand:" if is_dealer else "Your Hand:", ', '.join(hand))

def play_blackjack():
    """Plays a game of Blackjack."""

    deck = create_deck()
    player_hand = []
    dealer_hand = []

    # Deal initial hands
    for _ in range(2):
        card, deck = deal_card(deck)
        player_hand.append(card)
        card, deck = deal_card(deck)
        dealer_hand.append(card)

    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    print("\nWelcome to Blackjack!")
    display_hand(player_hand)
    display_hand(dealer_hand, is_dealer=True, hide_first_card=True)
    print(f"Your hand value: {player_value}")


    # Player's turn
    while player_value < 21:
        action = input("Hit or Stand? (h/s): ").lower()
        if action == 'h':
            card, deck = deal_card(deck)
            player_hand.append(card)
            player_value = calculate_hand_value(player_hand)
            display_hand(player_hand)
            print(f"Your hand value: {player_value}")
            if player_value > 21:
                print("Bust! You lose.")
                return
        elif action == 's':
            break
        else:
            print("Invalid input. Please enter 'h' or 's'.")

    # Dealer's turn
    if player_value <= 21:
        print("\nDealer's turn...")
        display_hand(dealer_hand, is_dealer=True)
        print(f"Dealer's hand value: {dealer_value}")

        while dealer_value < 17:
            print("Dealer hits.")
            card, deck = deal_card(deck)
            dealer_hand.append(card)
            dealer_value = calculate_hand_value(dealer_hand)
            display_hand(dealer_hand, is_dealer=True)
            print(f"Dealer's hand value: {dealer_value}")
            if dealer_value > 21:
                print("Dealer busts! You win!")
                return

        # Determine the winner
        print("\nFinal Results:")
        display_hand(player_hand)
        print(f"Your hand value: {player_value}")
        display_hand(dealer_hand, is_dealer=True)
        print(f"Dealer's hand value: {dealer_value}")

        if dealer_value > player_value:
            print("Dealer wins!")
        elif dealer_value == player_value:
            print("Push! (Tie)")
        else:
            print("You win!")


if __name__ == "__main__":
    play_blackjack()