import random

class Blackjack:
    """
    A class to represent a Blackjack game.
    """

    SUITS = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
    RANKS = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
             'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    VALUES = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6,
              'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
              'Queen': 10, 'King': 10, 'Ace': 11}

    def __init__(self):
        """
        Initializes a new Blackjack game.
        """
        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []
        self.player_total = 0
        self.dealer_total = 0
        self.player_aces = 0
        self.dealer_aces = 0
        self.game_over = False

    def create_deck(self):
        """
        Creates a standard 52-card deck.
        """
        deck = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                deck.append((suit, rank))
        random.shuffle(deck)
        return deck

    def deal_card(self, hand):
        """
        Deals a card from the deck to the specified hand.
        """
        suit, rank = self.deck.pop()
        hand.append((suit, rank))
        return suit, rank

    def calculate_hand_value(self, hand):
        """
        Calculates the total value of a hand.
        """
        total = 0
        aces = 0
        for suit, rank in hand:
            value = self.VALUES[rank]
            total += value
            if rank == 'Ace':
                aces += 1

        while total > 21 and aces > 0:
            total -= 10
            aces -= 1

        return total, aces

    def deal_initial_hands(self):
        """
        Deals the initial hands to the player and the dealer.
        """
        for _ in range(2):
            suit, rank = self.deal_card(self.player_hand)
            self.player_total, self.player_aces = self.calculate_hand_value(self.player_hand)
            suit, rank = self.deal_card(self.dealer_hand)
            self.dealer_total, self.dealer_aces = self.calculate_hand_value(self.dealer_hand)

    def hit(self):
        """
        Deals a card to the player's hand and updates the player's total.
        """
        suit, rank = self.deal_card(self.player_hand)
        self.player_total, self.player_aces = self.calculate_hand_value(self.player_hand)
        if self.player_total > 21:
            print("Bust! Player loses.")
            self.game_over = True

    def dealer_play(self):
        """
        The dealer's turn to play.
        """
        while self.dealer_total < 17:
            suit, rank = self.deal_card(self.dealer_hand)
            self.dealer_total, self.dealer_aces = self.calculate_hand_value(self.dealer_hand)
            print(f"Dealer hits. Dealer's hand: {self.dealer_hand}, Total: {self.dealer_total}")
            if self.dealer_total > 21:
                print("Dealer busts! Player wins.")
                self.game_over = True
                return

    def determine_winner(self):
        """
        Determines the winner of the game.
        """
        if self.player_total > self.dealer_total or self.dealer_total > 21:
            print("Player wins!")
        elif self.player_total == self.dealer_total:
            print("It's a push!")
        else:
            print("Dealer wins!")

    def print_hands(self, show_dealer_full=False):
        """
        Prints the player's and dealer's hands.
        """
        print(f"Player's hand: {self.player_hand}, Total: {self.player_total}")
        if show_dealer_full:
            print(f"Dealer's hand: {self.dealer_hand}, Total: {self.dealer_total}")
        else:
            print(f"Dealer's hand: [Hidden card, {self.dealer_hand[1]}], Total: ?")

    def play_game(self):
        """
        The main game loop.
        """
        self.deal_initial_hands()
        print("Welcome to Blackjack!")
        self.print_hands()

        while not self.game_over:
            action = input("Hit or Stand? (h/s): ").lower()
            if action == 'h':
                self.hit()
                self.print_hands()
                if self.game_over:
                    break
            elif action == 's':
                print("Player stands.")
                self.dealer_play()
                if not self.game_over:
                    self.print_hands(show_dealer_full=True)
                    self.determine_winner()
                self.game_over = True
            else:
                print("Invalid action. Please enter 'h' or 's'.")

        print("Game over!")


if __name__ == "__main__":
    game = Blackjack()
    game.play_game()