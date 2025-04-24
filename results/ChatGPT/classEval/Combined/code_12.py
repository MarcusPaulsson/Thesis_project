import random

class BlackjackGame:
    """
    A class representing a game of blackjack, which includes creating a deck, calculating the value of a hand, 
    and determining the winner based on the hand values of the player and dealer.
    """

    def __init__(self):
        """
        Initialize the Blackjack Game with a deck, player_hand, and dealer_hand.
        The deck stores 52 cards in random order, with Jokers removed.
        """
        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []

    def create_deck(self):
        """
        Create a deck of 52 cards without Jokers.
        :return: a shuffled list of 52 cards in the format ['AS', '2S', ...].
        """
        suits = ['S', 'C', 'D', 'H']
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        deck = [rank + suit for suit in suits for rank in ranks]
        random.shuffle(deck)
        return deck

    def calculate_hand_value(self, hand):
        """
        Calculate the value of the cards in the hand according to Blackjack rules.
        :param hand: list of cards
        :return: the total value of the hand
        """
        value = 0
        aces_count = 0

        for card in hand:
            rank = card[:-1]  # Get the rank part of the card
            if rank in ['J', 'Q', 'K']:
                value += 10
            elif rank == 'A':
                value += 11
                aces_count += 1
            else:
                value += int(rank)

        # Adjust for Aces if value exceeds 21
        while value > 21 and aces_count:
            value -= 10
            aces_count -= 1

        return value

    def check_winner(self, player_hand, dealer_hand):
        """
        Determine the winner by comparing the hand values of the player and dealer.
        :param player_hand: list of player's cards
        :param dealer_hand: list of dealer's cards
        :return: a string indicating the winner ('Dealer wins' or 'Player wins')
        """
        player_value = self.calculate_hand_value(player_hand)
        dealer_value = self.calculate_hand_value(dealer_hand)

        if player_value > 21:
            return 'Dealer wins'
        if dealer_value > 21:
            return 'Player wins'
        
        if player_value > dealer_value:
            return 'Player wins'
        else:
            return 'Dealer wins'