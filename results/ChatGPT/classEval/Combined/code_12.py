import random

class BlackjackGame:
    """
    Class representing a game of blackjack, including deck creation, hand value calculation, and winner determination.
    """

    def __init__(self):
        """
        Initialize the Blackjack Game with attributes for the deck, player hand, and dealer hand.
        """
        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []

    def create_deck(self):
        """
        Create a shuffled deck of 52 cards (without Jokers).
        :return: A list of 52 cards in random order.
        """
        suits = ['S', 'C', 'D', 'H']
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        deck = [rank + suit for suit in suits for rank in ranks]
        random.shuffle(deck)
        return deck

    def calculate_hand_value(self, hand):
        """
        Calculate the total value of a hand according to Blackjack rules.
        :param hand: List of cards in the hand.
        :return: Total value of the hand.
        """
        value = 0
        aces = 0
        
        for card in hand:
            rank = card[:-1]  # Extract the rank part of the card
            if rank in ['J', 'Q', 'K']:
                value += 10
            elif rank == 'A':
                value += 11
                aces += 1
            else:
                value += int(rank)

        # Adjust for Aces if the total value exceeds 21
        while value > 21 and aces:
            value -= 10
            aces -= 1

        return value

    def check_winner(self, player_hand, dealer_hand):
        """
        Determine the winner by comparing the hand values of the player and dealer.
        :param player_hand: List of player's cards.
        :param dealer_hand: List of dealer's cards.
        :return: Result of the game as a string indicating the winner.
        """
        player_value = self.calculate_hand_value(player_hand)
        dealer_value = self.calculate_hand_value(dealer_hand)

        if player_value > 21:
            return 'Dealer wins'
        if dealer_value > 21:
            return 'Player wins'
        if player_value > dealer_value:
            return 'Player wins'
        return 'Dealer wins'