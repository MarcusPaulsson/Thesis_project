import random

class Card:
    SUITS = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
    RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')
    VALUES = {rank: min(value, 10) for value, rank in enumerate(RANKS, start=2)}
    VALUES['Ace'] = 11  # Ace can be 1 or 11, handled in hand value calculation.

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Card.SUITS for rank in Card.RANKS]
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop() if self.cards else None

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def calculate_value(self):
        value = sum(Card.VALUES[card.rank] for card in self.cards)
        # Adjust for Aces
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
            self.player_hand.add_card(self.deck.deal_card())
            self.dealer_hand.add_card(self.deck.deal_card())

    def display_hands(self, reveal_dealer=False):
        print(f"Player's Hand: {self.player_hand} (Value: {self.player_hand.calculate_value()})")
        if reveal_dealer:
            print(f"Dealer's Hand: {self.dealer_hand} (Value: {self.dealer_hand.calculate_value()})")
        else:
            print(f"Dealer's Hand: {self.dealer_hand.cards[0]}, Hidden Card")

    def player_turn(self):
        while True:
            self.display_hands()
            action = input("Do you want to (h)it or (s)tand? ").lower()
            if action == 'h':
                self.player_hand.add_card(self.deck.deal_card())
                if self.player_hand.calculate_value() > 21:
                    print("You busted!")
                    return False
            elif action == 's':
                break
        return True

    def dealer_turn(self):
        while self.dealer_hand.calculate_value() < 17:
            self.dealer_hand.add_card(self.deck.deal_card())

    def determine_winner(self):
        player_value = self.player_hand.calculate_value()
        dealer_value = self.dealer_hand.calculate_value()
        print(f"Final Player's Hand: {self.player_hand} (Value: {player_value})")
        print(f"Final Dealer's Hand: {self.dealer_hand} (Value: {dealer_value})")

        if player_value > 21:
            return "Dealer wins!"
        elif dealer_value > 21 or player_value > dealer_value:
            return "Player wins!"
        elif player_value < dealer_value:
            return "Dealer wins!"
        else:
            return "It's a tie!"

    def play(self):
        print("Welcome to Blackjack!")
        self.initial_deal()
        if self.player_turn():
            self.dealer_turn()
        print(self.determine_winner())

if __name__ == "__main__":
    game = Blackjack()
    game.play()