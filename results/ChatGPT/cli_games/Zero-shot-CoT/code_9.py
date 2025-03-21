import random

class Card:
    """Represents a single playing card."""
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def value(self):
        """Returns the value of the card."""
        if self.rank in ['J', 'Q', 'K']:
            return 10
        elif self.rank == 'A':
            return 11
        else:
            return int(self.rank)

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    """Represents a deck of 52 playing cards."""
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']
                      for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']]
        random.shuffle(self.cards)

    def deal_card(self):
        """Deals a card from the deck."""
        return self.cards.pop() if self.cards else None


class Hand:
    """Represents a player's hand of cards."""
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        """Adds a card to the hand."""
        self.cards.append(card)

    def value(self):
        """Calculates the total value of the hand."""
        total = sum(card.value() for card in self.cards)
        aces = sum(1 for card in self.cards if card.rank == 'A')
        
        while total > 21 and aces:
            total -= 10
            aces -= 1
            
        return total

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)


class Blackjack:
    """Implements the Blackjack game logic."""
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()

    def deal_initial_cards(self):
        """Deals initial cards to player and dealer."""
        for _ in range(2):
            self.player_hand.add_card(self.deck.deal_card())
            self.dealer_hand.add_card(self.deck.deal_card())

    def player_turn(self):
        """Handles the player's turn."""
        while True:
            print(f"Your hand: {self.player_hand} (Value: {self.player_hand.value()})")
            if self.player_hand.value() > 21:
                print("Bust! You lose.")
                return False
            
            action = input("Do you want to (h)it or (s)tand? ").lower()
            if action == 'h':
                self.player_hand.add_card(self.deck.deal_card())
            elif action == 's':
                break
            else:
                print("Invalid input. Please enter 'h' or 's'.")
        return True

    def dealer_turn(self):
        """Handles the dealer's turn."""
        while self.dealer_hand.value() < 17:
            self.dealer_hand.add_card(self.deck.deal_card())

    def determine_winner(self):
        """Determines the winner of the game."""
        player_value = self.player_hand.value()
        dealer_value = self.dealer_hand.value()

        print(f"Dealer's hand: {self.dealer_hand} (Value: {dealer_value})")
        if dealer_value > 21 or player_value > dealer_value:
            print("You win!")
        elif player_value < dealer_value:
            print("You lose!")
        else:
            print("It's a tie!")

    def play(self):
        """Starts the game of Blackjack."""
        self.deal_initial_cards()
        if self.player_turn():
            self.dealer_turn()
            self.determine_winner()


if __name__ == "__main__":
    game = Blackjack()
    game.play()