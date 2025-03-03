import random

# Constants
SUITS = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')
VALUES = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11
}

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
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += VALUES[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
        self.adjust_for_aces()

    def adjust_for_aces(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)

class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()

    def initial_deal(self):
        for _ in range(2):
            self.player_hand.add_card(self.deck.deal_card())
            self.dealer_hand.add_card(self.deck.deal_card())

    def show_hands(self, hide_dealer_card=True):
        print("Player's Hand:", self.player_hand)
        if hide_dealer_card:
            print("Dealer's Hand: [Hidden],", self.dealer_hand.cards[1])
        else:
            print("Dealer's Hand:", self.dealer_hand)

    def player_busts(self):
        print("Player busts! Dealer wins.")

    def dealer_busts(self):
        print("Dealer busts! Player wins.")

    def dealer_turn(self):
        while self.dealer_hand.value < 17:
            self.dealer_hand.add_card(self.deck.deal_card())

    def determine_winner(self):
        if self.player_hand.value > 21:
            self.player_busts()
        elif self.dealer_hand.value > 21:
            self.dealer_busts()
        elif self.player_hand.value > self.dealer_hand.value:
            print("Player wins!")
        elif self.player_hand.value < self.dealer_hand.value:
            print("Dealer wins!")
        else:
            print("It's a tie!")

    def play(self):
        self.initial_deal()
        self.show_hands()

        while True:
            action = input("Would you like to [H]it or [S]tand? ").strip().lower()
            if action == 'h':
                self.player_hand.add_card(self.deck.deal_card())
                print("Player's Hand:", self.player_hand)
                if self.player_hand.value > 21:
                    self.player_busts()
                    return
            elif action == 's':
                break
            else:
                print("Invalid input! Please enter 'H' or 'S'.")

        self.dealer_turn()
        self.show_hands(hide_dealer_card=False)
        self.determine_winner()

if __name__ == "__main__":
    game = BlackjackGame()
    game.play()