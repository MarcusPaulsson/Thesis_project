import random

class BlackjackGame:
    """
    This is a class representing a game of blackjack, which includes creating a deck, calculating the value of a hand,
    and determine the winner based on the hand values of the player and dealer.
    """

    def __init__(self):
        """
        Initialize the Blackjack Game with the attribute deck, player_hand and dealer_hand. While initializing deck attribute,
        call the create_deck method to generate. The deck stores 52 rondom order poker with the Jokers removed, format is ['AS', '2S', ...].
        """
        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []

    def create_deck(self):
        """
        Create a deck of 52 cards, which stores 52 rondom order poker with the Jokers removed.
        :return: a list of 52 random order poker with the Jokers removed, format is ['AS', '2S', ...].
        """
        return sorted(["{}{}".format(rank, suit) for rank in "A23456789TJQK" for suit in "CDHS"] * 2 + ["10{}".format(suit) for suit in "CDHS"] + ["JS", "BS"])


    def calculate_hand_value(self, hand):
        """
        Calculate the value of the poker cards stored in hand list according to the rules of the Blackjack Game.
        If the card is a digit, its value is added to the total hand value. Value of J, Q, or K is 10, while Aces are worth 11.
        If the total hand value exceeds 21 and there are Aces present, one Ace is treated as having a value of 1 instead of 11,
        until the hand value is less than or equal to 21, or all Aces have been counted as value of 1.
        :param hand: list
        :return: the value of the poker cards stored in hand list, a number.
        """
        total = 0
        aces_count = 0
        for card in hand:
            if card[0] == 'A':
                total += 11
                aces_count += 1
            elif card[0] in "JQK":
                total += 10
            else:
                total += int(card[:-1])
        while total > 21 and aces_count > 0:
            total -= 10
            aces_count -= 1
        return total

    def check_winner(self, player_hand, dealer_hand):
        """
        Determines the winner of a game by comparing the hand values of the player and dealer.
        :param player_hand: list
        :param dealer_hand: list
        :return: the result of the game, only two certain str: 'Dealer wins' or 'Player wins'
        """
        if self.calculate_hand_value(player_hand) > 21 and self.calculate_hand_value(dealer_hand) <= 21:
            return "Dealer wins"
        elif self.calculate_hand_value(player_hand) < 21 and self.calculate_hand_value(dealer_hand) > 21:
            return "Player wins"
        else:
            if abs(self.calculate_hand_value(player_hand) - 21) <= abs(self.calculate_hand_value(dealer_hand) - 21):
                return "Player wins"
            else:
                return "Dealer wins"