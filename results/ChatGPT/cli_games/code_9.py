import random

# Constants
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def calculate_value(self):
        value = sum(VALUES[card.rank] for card in self.cards)
        aces = sum(1 for card in self.cards if card.rank == 'Ace')

        while value > 21 and aces:
            value -= 10
            aces -= 1

        return value

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)

def main():
    print("Welcome to Blackjack!")
    
    while True:
        deck = Deck()
        player_hand = Hand()
        dealer_hand = Hand()

        # Initial dealing
        for _ in range(2):
            player_hand.add_card(deck.deal_card())
            dealer_hand.add_card(deck.deal_card())

        # Player's turn
        while True:
            print(f"Your hand: {player_hand} (Value: {player_hand.calculate_value()})")
            print(f"Dealer's hand: {dealer_hand.cards[0]}, [Hidden]")

            if player_hand.calculate_value() == 21:
                print("Blackjack! You win!")
                break
            elif player_hand.calculate_value() > 21:
                print("Bust! You lose!")
                break

            action = input("Do you want to (h)it or (s)tand? ").lower()
            if action == 'h':
                player_hand.add_card(deck.deal_card())
            elif action == 's':
                break

        # Dealer's turn
        if player_hand.calculate_value() <= 21:
            while dealer_hand.calculate_value() < 17:
                dealer_hand.add_card(deck.deal_card())

            print(f"Dealer's hand: {dealer_hand} (Value: {dealer_hand.calculate_value()})")

            # Determine winner
            player_value = player_hand.calculate_value()
            dealer_value = dealer_hand.calculate_value()

            if dealer_value > 21 or player_value > dealer_value:
                print("You win!")
            elif player_value < dealer_value:
                print("You lose!")
            else:
                print("It's a tie!")

        # Play again?
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break

if __name__ == "__main__":
    main()