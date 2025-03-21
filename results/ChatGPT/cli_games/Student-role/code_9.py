import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def value(self):
        if self.rank in ['Jack', 'Queen', 'King']:
            return 10
        elif self.rank == 'Ace':
            return 11
        else:
            return int(self.rank)

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']
                      for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']]
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def value(self):
        total = sum(card.value() for card in self.cards)
        aces = sum(1 for card in self.cards if card.rank == 'Ace')
        while total > 21 and aces:
            total -= 10
            aces -= 1
        return total

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)

class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()

    def start_game(self):
        print("Welcome to Blackjack!")
        self.player_hand.add_card(self.deck.deal())
        self.player_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())
        self.player_turn()

    def player_turn(self):
        while True:
            print(f"\nYour hand: {self.player_hand} (Value: {self.player_hand.value()})")
            print(f"Dealer's hand: {self.dealer_hand.cards[0]} and [Hidden]")
            if self.player_hand.value() > 21:
                print("You bust! Dealer wins.")
                return
            action = input("Would you like to (H)it or (S)tand? ").strip().lower()
            if action == 'h':
                self.player_hand.add_card(self.deck.deal())
            elif action == 's':
                break

        self.dealer_turn()

    def dealer_turn(self):
        print(f"\nDealer's hand: {self.dealer_hand} (Value: {self.dealer_hand.value()})")
        while self.dealer_hand.value() < 17:
            self.dealer_hand.add_card(self.deck.deal())
            print(f"Dealer hits: {self.dealer_hand} (Value: {self.dealer_hand.value()})")
        
        self.determine_winner()

    def determine_winner(self):
        player_value = self.player_hand.value()
        dealer_value = self.dealer_hand.value()
        print(f"\nFinal Player Hand: {self.player_hand} (Value: {player_value})")
        print(f"Final Dealer Hand: {self.dealer_hand} (Value: {dealer_value})")
        
        if dealer_value > 21 or player_value > dealer_value:
            print("You win!")
        elif player_value < dealer_value:
            print("Dealer wins!")
        else:
            print("It's a tie!")

if __name__ == "__main__":
    game = BlackjackGame()
    game.start_game()