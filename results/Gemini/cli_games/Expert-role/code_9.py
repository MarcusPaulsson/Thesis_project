import random

class Blackjack:
    """
    A class to represent a Blackjack game.
    """

    def __init__(self):
        """
        Initializes the Blackjack game.
        """
        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []
        self.player_score = 0
        self.dealer_score = 0
        self.game_over = False

    def create_deck(self):
        """
        Creates a standard 52-card deck.
        """
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        deck = [(rank, suit) for suit in suits for rank in ranks]
        random.shuffle(deck)
        return deck

    def deal_card(self, hand):
        """
        Deals a card from the deck to the given hand.
        """
        card = self.deck.pop()
        hand.append(card)
        return card

    def calculate_hand_value(self, hand):
        """
        Calculates the value of a hand, treating Aces as 1 or 11.
        """
        value = 0
        ace_count = 0
        for card in hand:
            rank = card[0]
            if rank.isdigit():
                value += int(rank)
            elif rank in ["Jack", "Queen", "King"]:
                value += 10
            elif rank == "Ace":
                value += 11
                ace_count += 1

        while value > 21 and ace_count > 0:
            value -= 10
            ace_count -= 1

        return value

    def display_hand(self, hand, is_dealer=False, hide_first_card=False):
        """
        Displays a hand of cards.
        """
        if is_dealer and hide_first_card:
            print("Dealer's Hand: [Hidden Card]", end=" ")
            for card in hand[1:]:
                print(f"[{card[0]} of {card[1]}]", end=" ")
            print()
        else:
            if is_dealer:
                print("Dealer's Hand:", end=" ")
            else:
                print("Your Hand:", end=" ")
            for card in hand:
                print(f"[{card[0]} of {card[1]}]", end=" ")
            print()

    def player_turn(self):
        """
        Handles the player's turn.
        """
        while True:
            self.display_hand(self.player_hand)
            self.player_score = self.calculate_hand_value(self.player_hand)
            print(f"Your Score: {self.player_score}")

            if self.player_score > 21:
                print("You busted!")
                self.game_over = True
                return

            action = input("Hit or Stand? (h/s): ").lower()
            if action == "h":
                self.deal_card(self.player_hand)
            elif action == "s":
                break
            else:
                print("Invalid input. Please enter 'h' or 's'.")

    def dealer_turn(self):
        """
        Handles the dealer's turn.
        """
        print("\nDealer's Turn:")
        while self.dealer_score < 17:
            self.deal_card(self.dealer_hand)
            self.dealer_score = self.calculate_hand_value(self.dealer_hand)
            self.display_hand(self.dealer_hand, is_dealer=True)
            print(f"Dealer's Score: {self.dealer_score}")
            if self.dealer_score > 21:
                print("Dealer busted!")
                return

    def determine_winner(self):
        """
        Determines the winner of the game.
        """
        print("\n--- Game Over ---")
        self.display_hand(self.player_hand)
        print(f"Your Score: {self.player_score}")
        self.display_hand(self.dealer_hand, is_dealer=True)
        print(f"Dealer's Score: {self.dealer_score}")

        if self.player_score > 21:
            print("Dealer wins!")
        elif self.dealer_score > 21:
            print("You win!")
        elif self.player_score > self.dealer_score:
            print("You win!")
        elif self.dealer_score > self.player_score:
            print("Dealer wins!")
        else:
            print("It's a tie!")

    def play_again(self):
        """
        Asks if the player wants to play again.
        """
        while True:
            play_again = input("Play again? (y/n): ").lower()
            if play_again == "y":
                self.__init__()  # Reset the game
                self.start_game()
                break
            elif play_again == "n":
                print("Thanks for playing!")
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

    def start_game(self):
        """
        Starts the Blackjack game.
        """
        print("Welcome to Blackjack!")

        # Deal initial hands
        self.deal_card(self.player_hand)
        self.deal_card(self.dealer_hand)
        self.deal_card(self.player_hand)
        self.deal_card(self.dealer_hand)

        # Display initial hands (dealer's first card hidden)
        self.display_hand(self.player_hand)
        self.display_hand(self.dealer_hand, is_dealer=True, hide_first_card=True)

        # Player's turn
        self.player_turn()

        # Dealer's turn (if player didn't bust)
        if not self.game_over:
            self.dealer_score = self.calculate_hand_value(self.dealer_hand)
            self.dealer_turn()

        # Determine the winner
        if not self.game_over:
             self.player_score = self.calculate_hand_value(self.player_hand) #recalculate in case player has ace
             self.determine_winner()

        # Ask to play again
        self.play_again()


if __name__ == "__main__":
    game = Blackjack()
    game.start_game()