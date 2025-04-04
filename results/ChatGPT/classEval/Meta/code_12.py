import random

class BlackjackGame:
    """
    This is a class representing a game of blackjack, which includes creating a deck, calculating the value of a hand, and determining the winner based on the hand values of the player and dealer.
    """

    def __init__(self):
        """
        Initialize the Blackjack Game with the attribute deck, player_hand and dealer_hand.
        While initializing deck attribute, call the create_deck method to generate.
        The deck stores 52 random order poker with the Jokers removed, format is ['AS', '2S', ...].
        """
        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []

    def create_deck(self):
        """
        Create a deck of 52 cards, which stores 52 random order poker with the Jokers removed.
        :return: a list of 52 random order poker with the Jokers removed, format is ['AS', '2S', ...].
        """
        suits = ['H', 'D', 'C', 'S']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        deck = [value + suit for suit in suits for value in values]
        random.shuffle(deck)
        return deck

    def calculate_hand_value(self, hand):
        """
        Calculate the value of the poker cards stored in hand list according to the rules of the Blackjack Game.
        :param hand: list
        :return: the value of the poker cards stored in hand list, a number.
        """
        value = 0
        aces = 0
        
        for card in hand:
            rank = card[:-1]  # Get the rank part of the card
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
        Determines the winner of a game by comparing the hand values of the player and dealer.
        :param player_hand: list
        :param dealer_hand: list
        :return: the result of the game, only two certain str: 'Dealer wins' or 'Player wins'
        """
        player_value = self.calculate_hand_value(player_hand)
        dealer_value = self.calculate_hand_value(dealer_hand)

        if player_value > 21:
            return 'Dealer wins'
        if dealer_value > 21:
            return 'Player wins'
        
        if player_value == dealer_value:
            return 'Dealer wins'  # Assuming dealer wins in case of a tie
        return 'Player wins' if player_value > dealer_value else 'Dealer wins'