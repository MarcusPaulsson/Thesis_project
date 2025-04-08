import random

class BlackjackGame:
    """
    A class representing a Blackjack game.
    """

    def __init__(self):
        """
        Initializes the game with a shuffled deck and empty hands for the player and dealer.
        """
        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []

    def create_deck(self):
        """
        Creates a standard 52-card deck and shuffles it.

        Returns:
            list: A list of strings representing the deck of cards.  Each card is a string of the form "RankSuit", e.g., "AS" (Ace of Spades).
        """
        suits = ['S', 'C', 'D', 'H']  # Spades, Clubs, Diamonds, Hearts
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        deck = [rank + suit for suit in suits for rank in ranks]
        random.shuffle(deck)
        return deck

    def calculate_hand_value(self, hand):
        """
        Calculates the value of a hand in Blackjack.  Aces can be 1 or 11.

        Args:
            hand (list): A list of strings representing the cards in the hand.

        Returns:
            int: The calculated value of the hand.
        """
        value = 0
        aces = 0
        for card in hand:
            rank = card[:-1]  # Extract the rank from the card string
            if rank.isdigit():
                value += int(rank)
            elif rank in ['J', 'Q', 'K']:
                value += 10
            elif rank == 'A':
                value += 11
                aces += 1

        # Adjust for Aces if the hand value is over 21
        while value > 21 and aces > 0:
            value -= 10
            aces -= 1

        return value

    def check_winner(self, player_hand, dealer_hand):
        """
        Determines the winner of the Blackjack game based on the player's and dealer's hands.

        Args:
            player_hand (list): The player's hand (list of card strings).
            dealer_hand (list): The dealer's hand (list of card strings).

        Returns:
            str: "Player wins" or "Dealer wins" indicating the winner.
        """
        player_value = self.calculate_hand_value(player_hand)
        dealer_value = self.calculate_hand_value(dealer_hand)

        if player_value > 21 and dealer_value > 21:
            # Both busted, the dealer wins
            return 'Dealer wins'
        elif player_value > 21:
            return 'Dealer wins'
        elif dealer_value > 21:
            return 'Player wins'
        else:
            if player_value > dealer_value:
                return 'Player wins'
            elif dealer_value > player_value:
                return 'Dealer wins'
            else:
                # It's a tie, the dealer wins in Blackjack
                return 'Dealer wins'