import random

class BlackjackGame:
    """
    This class represents a game of blackjack, including deck creation, hand value calculation, and winner determination.
    """

    def __init__(self):
        """
        Initializes the Blackjack Game with attributes deck, player_hand, and dealer_hand.
        Calls the create_deck method to generate the deck.
        """
        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []

    def create_deck(self):
        """
        Creates a deck of 52 cards, removing Jokers.
        :return: A shuffled list of 52 cards (format: ['AS', '2S', ...]).
        """
        suits = ['S', 'H', 'D', 'C']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        deck = [rank + suit for suit in suits for rank in ranks]
        random.shuffle(deck)
        return deck

    def calculate_hand_value(self, hand):
        """
        Calculates the value of the poker cards in a hand according to Blackjack rules.
        :param hand: List of cards.
        :return: The total value of the hand.
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
        Determines the winner by comparing the hand values of the player and dealer.
        :param player_hand: List of player's cards.
        :param dealer_hand: List of dealer's cards.
        :return: A string indicating the result: 'Dealer wins' or 'Player wins'.
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