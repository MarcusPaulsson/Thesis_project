import random

class BlackjackGame:
    """
    This class represents a game of blackjack, including creating a deck,
    calculating the value of a hand, and determining the winner based on the hand values
    of the player and dealer.
    """

    def __init__(self):
        """
        Initialize the Blackjack Game with attributes for the deck, player's hand, and dealer's hand.
        """
        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []

    def create_deck(self):
        """
        Create and shuffle a deck of 52 cards (without Jokers).
        :return: A shuffled list of 52 cards in the format ['AS', '2S', ...].
        """
        suits = ['S', 'C', 'D', 'H']
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        deck = [f"{rank}{suit}" for suit in suits for rank in ranks]
        random.shuffle(deck)
        return deck

    def calculate_hand_value(self, hand):
        """
        Calculate the value of the cards in the given hand according to Blackjack rules.
        :param hand: List of cards in the player's or dealer's hand.
        :return: The total value of the hand as an integer.
        """
        value = 0
        aces = 0

        for card in hand:
            rank = card[:-1]
            if rank in ['J', 'Q', 'K']:
                value += 10
            elif rank == 'A':
                aces += 1
                value += 11
            else:
                value += int(rank)

        while value > 21 and aces:
            value -= 10
            aces -= 1

        return value

    def check_winner(self, player_hand, dealer_hand):
        """
        Determine the winner between the player and dealer based on their hand values.
        :param player_hand: List of cards in the player's hand.
        :param dealer_hand: List of cards in the dealer's hand.
        :return: A string indicating the winner: 'Dealer wins' or 'Player wins'.
        """
        player_value = self.calculate_hand_value(player_hand)
        dealer_value = self.calculate_hand_value(dealer_hand)

        if player_value > 21:
            return 'Dealer wins'
        elif dealer_value > 21:
            return 'Player wins'
        elif player_value > dealer_value:
            return 'Player wins'
        else:
            return 'Dealer wins'