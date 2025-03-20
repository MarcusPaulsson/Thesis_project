import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = self.get_value()

    def get_value(self):
        if self.rank in ['J', 'Q', 'K']:
            return 10
        elif self.rank == 'A':
            return 11  # Initially count Ace as 11
        else:
            return int(self.rank)

    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']
                      for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']]
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == 'A':
            self.aces += 1
        self.adjust_for_ace()

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()

    def start_game(self):
        for _ in range(2):
            self.player_hand.add_card(self.deck.deal_card())
            self.dealer_hand.add_card(self.deck.deal_card())
        self.show_hands(initial=True)
        self.player_turn()

    def show_hands(self, initial=False):
        print("\nDealer's Hand:")
        if initial:
            print(" <hidden card> ")
            print(" " + str(self.dealer_hand.cards[1]))
        else:
            for card in self.dealer_hand.cards:
                print(" " + str(card))
        print("\nYour Hand:")
        for card in self.player_hand.cards:
            print(" " + str(card))
        print(f"Your total value: {self.player_hand.value}")

    def player_turn(self):
        while self.player_hand.value < 21:
            action = input("Would you like to hit or stand? (h/s): ").lower()
            if action == 'h':
                self.player_hand.add_card(self.deck.deal_card())
                self.show_hands()
            elif action == 's':
                break
            else:
                print("Invalid input. Please enter 'h' or 's'.")
        self.dealer_turn()

    def dealer_turn(self):
        print("\nDealer's turn.")
        self.show_hands()
        while self.dealer_hand.value < 17:
            print("Dealer hits.")
            self.dealer_hand.add_card(self.deck.deal_card())
            self.show_hands()
        self.determine_winner()

    def determine_winner(self):
        print("\nFinal Hands:")
        self.show_hands(initial=False)
        if self.player_hand.value > 21:
            print("You bust! Dealer wins.")
        elif self.dealer_hand.value > 21:
            print("Dealer busts! You win!")
        elif self.player_hand.value > self.dealer_hand.value:
            print("You win!")
        elif self.player_hand.value < self.dealer_hand.value:
            print("Dealer wins!")
        else:
            print("It's a tie!")

if __name__ == "__main__":
    game = BlackjackGame()
    game.start_game()