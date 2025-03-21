import random

class Blackjack:
    def __init__(self):
        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []
        self.player_score = 0
        self.dealer_score = 0

    def create_deck(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        deck = []
        for suit in suits:
            for rank in ranks:
                deck.append((rank, suit))
        random.shuffle(deck)
        return deck

    def deal_card(self, hand):
        card = self.deck.pop()
        hand.append(card)
        return card

    def calculate_hand_value(self, hand):
        value = 0
        ace_count = 0
        for card in hand:
            rank = card[0]
            if rank.isdigit():
                value += int(rank)
            elif rank in ["Jack", "Queen", "King"]:
                value += 10
            else:  # Ace
                value += 11
                ace_count += 1

        while value > 21 and ace_count > 0:
            value -= 10
            ace_count -= 1

        return value

    def display_hand(self, hand, is_dealer=False, hide_first=False):
        if is_dealer:
            print("Dealer's hand:")
            if hide_first:
                print("[Hidden Card]", end=" ")
                for i in range(1, len(hand)):
                    print(f"{hand[i][0]} of {hand[i][1]}", end=" ")
            else:
                for card in hand:
                    print(f"{card[0]} of {card[1]}", end=" ")
        else:
            print("Your hand:")
            for card in hand:
                print(f"{card[0]} of {card[1]}", end=" ")
        print()

    def play_round(self):
        # Deal initial hands
        self.deal_card(self.player_hand)
        self.deal_card(self.dealer_hand)
        self.deal_card(self.player_hand)
        self.deal_card(self.dealer_hand)

        self.player_score = self.calculate_hand_value(self.player_hand)
        self.dealer_score = self.calculate_hand_value(self.dealer_hand)

        # Player's turn
        self.display_hand(self.player_hand)
        self.display_hand(self.dealer_hand, is_dealer=True, hide_first=True)

        while self.player_score < 21:
            action = input("Hit or Stand? (h/s): ").lower()
            if action == 'h':
                card = self.deal_card(self.player_hand)
                self.player_score = self.calculate_hand_value(self.player_hand)
                print(f"You drew: {card[0]} of {card[1]}")
                self.display_hand(self.player_hand)
                if self.player_score > 21:
                    print("Bust!")
                    return "dealer" # Dealer wins
            elif action == 's':
                break  # Player stands
            else:
                print("Invalid action. Please enter 'h' or 's'.")

        # Dealer's turn
        if self.player_score <= 21:
            print("\nDealer's turn:")
            self.display_hand(self.dealer_hand, is_dealer=True)
            while self.dealer_score < 17:
                card = self.deal_card(self.dealer_hand)
                self.dealer_score = self.calculate_hand_value(self.dealer_hand)
                print(f"Dealer drew: {card[0]} of {card[1]}")
                self.display_hand(self.dealer_hand, is_dealer=True)
                if self.dealer_score > 21:
                    print("Dealer busts!")
                    return "player"  # Player wins

        # Determine the winner
        print("\nFinal scores:")
        print(f"Your score: {self.player_score}")
        print(f"Dealer's score: {self.dealer_score}")

        if self.player_score > 21:
            return "dealer"
        elif self.dealer_score > 21:
            return "player"
        elif self.player_score > self.dealer_score:
            return "player"
        elif self.dealer_score > self.player_score:
            return "dealer"
        else:
            return "tie"

    def play_game(self):
        while True:
            self.deck = self.create_deck()  # Reset the deck
            self.player_hand = []
            self.dealer_hand = []
            self.player_score = 0
            self.dealer_score = 0

            result = self.play_round()

            if result == "player":
                print("You win!")
            elif result == "dealer":
                print("Dealer wins!")
            else:
                print("It's a tie!")

            play_again = input("Play again? (y/n): ").lower()
            if play_again != 'y':
                break

if __name__ == "__main__":
    game = Blackjack()
    game.play_game()