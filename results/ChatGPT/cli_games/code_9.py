import random

class Card:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def value(self):
        if self.rank in ['Jack', 'Queen', 'King']:
            return 10
        elif self.rank == 'Ace':
            return 11  # Ace is initially 11, will adjust later
        else:
            return int(self.rank)

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Card.suits for rank in Card.ranks]
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def value(self):
        value = sum(card.value() for card in self.cards)
        aces = sum(1 for card in self.cards if card.rank == 'Ace')
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)

class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()

    def initial_deal(self):
        for _ in range(2):
            self.player_hand.add_card(self.deck.deal())
            self.dealer_hand.add_card(self.deck.deal())

    def display_hands(self, reveal_dealer=False):
        print(f"Player's Hand: {self.player_hand} (Value: {self.player_hand.value()})")
        if reveal_dealer:
            print(f"Dealer's Hand: {self.dealer_hand} (Value: {self.dealer_hand.value()})")
        else:
            print(f"Dealer's Hand: {self.dealer_hand.cards[0]}, [Hidden]")

    def player_turn(self):
        while True:
            self.display_hands()
            if self.player_hand.value() > 21:
                print("Player busts! Dealer wins.")
                return False
            
            action = input("Do you want to (h)it or (s)tand? ").strip().lower()
            if action == 'h':
                self.player_hand.add_card(self.deck.deal())
            elif action == 's':
                break
            else:
                print("Invalid input! Please enter 'h' or 's'.")
        return True

    def dealer_turn(self):
        while self.dealer_hand.value() < 17:
            self.dealer_hand.add_card(self.deck.deal())

    def determine_winner(self):
        player_value = self.player_hand.value()
        dealer_value = self.dealer_hand.value()
        print(f"Final Hands:\nPlayer's Hand: {self.player_hand} (Value: {player_value})\nDealer's Hand: {self.dealer_hand} (Value: {dealer_value})")

        if dealer_value > 21 or player_value > dealer_value:
            print("Player wins!")
        elif player_value < dealer_value:
            print("Dealer wins!")
        else:
            print("It's a tie!")

    def play(self):
        print("Welcome to Blackjack!")
        self.initial_deal()
        if self.player_turn():
            self.dealer_turn()
            self.display_hands(reveal_dealer=True)
            self.determine_winner()

if __name__ == "__main__":
    game = Blackjack()
    game.play()