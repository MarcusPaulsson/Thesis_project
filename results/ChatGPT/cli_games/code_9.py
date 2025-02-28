import random

# Constants
CARD_VALUES = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = list(CARD_VALUES.keys())

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def value(self):
        return CARD_VALUES[self.rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in SUITS for rank in RANKS]
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop() if self.cards else None

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def value(self):
        value, aces = 0, 0
        for card in self.cards:
            value += card.value()
            if card.rank == 'A':
                aces += 1
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)

def play_blackjack():
    print("Welcome to Blackjack!")
    deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()

    # Initial dealing
    for _ in range(2):
        player_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

    while True:
        print(f"\nYour hand: {player_hand} (Value: {player_hand.value()})")
        print(f"Dealer's hand: {dealer_hand.cards[0]} and unknown card")

        if player_hand.value() == 21:
            print("Blackjack! You win!")
            return
        elif player_hand.value() > 21:
            print("Bust! You lose!")
            return

        action = input("Do you want to (h)it or (s)tand? ").lower()
        if action == 'h':
            player_hand.add_card(deck.deal())
        elif action == 's':
            break
        else:
            print("Invalid input. Please enter 'h' or 's'.")

    # Dealer's turn
    while dealer_hand.value() < 17:
        dealer_hand.add_card(deck.deal())

    print(f"\nDealer's hand: {dealer_hand} (Value: {dealer_hand.value()})")

    # Determine the outcome
    if dealer_hand.value() > 21:
        print("Dealer busts! You win!")
    elif player_hand.value() > dealer_hand.value():
        print("You win!")
    elif player_hand.value() < dealer_hand.value():
        print("You lose!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_blackjack()