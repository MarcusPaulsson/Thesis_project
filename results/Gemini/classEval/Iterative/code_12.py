import random

class BlackjackGame:
    """
    A class representing a game of blackjack.
    """

    def __init__(self):
        """
        Initializes the Blackjack Game with a deck, player hand, and dealer hand.
        """
        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []

    def create_deck(self):
        """
        Creates a shuffled deck of 52 cards.
        :return: A list representing the deck of cards.
        """
        suits = ['S', 'H', 'C', 'D']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        deck = [rank + suit for suit in suits for rank in ranks]
        random.shuffle(deck)
        return deck

    def calculate_hand_value(self, hand):
        """
        Calculates the value of a hand in Blackjack.
        :param hand: A list of cards in the hand.
        :return: The total value of the hand.
        """
        ace_count = 0
        total = 0
        for card in hand:
            rank = card[:-1]  # Extract the rank from the card string
            if rank.isdigit():
                total += int(rank)
            elif rank in ['J', 'Q', 'K']:
                total += 10
            else:
                total += 11
                ace_count += 1

        while total > 21 and ace_count > 0:
            total -= 10
            ace_count -= 1

        return total

    def check_winner(self, player_hand, dealer_hand):
        """
        Determines the winner of the game based on hand values.
        :param player_hand: The player's hand.
        :param dealer_hand: The dealer's hand.
        :return: "Player wins", "Dealer wins", or "Tie"
        """
        player_value = self.calculate_hand_value(player_hand)
        dealer_value = self.calculate_hand_value(dealer_hand)

        if player_value > 21:
            return 'Dealer wins'
        elif dealer_value > 21:
            return 'Player wins'
        elif player_value > dealer_value:
            return 'Player wins'
        elif dealer_value > player_value:
            return 'Dealer wins'
        else:
            return 'Tie'  # Corrected to return Tie in case of a tie