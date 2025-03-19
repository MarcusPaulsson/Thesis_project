import random

class Blackjack:
    def __init__(self):
        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []
        self.player_score = 0
        self.dealer_score = 0
        self.game_over = False

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

    def calculate_hand_score(self, hand):
        score = 0
        ace_count = 0
        for card in hand:
            rank = card[0]
            if rank.isdigit():
                score += int(rank)
            elif rank in ["Jack", "Queen", "King"]:
                score += 10
            elif rank == "Ace":
                score += 1
                ace_count += 1

        while score + 10 <= 21 and ace_count > 0:
            score += 10
            ace_count -= 1

        return score

    def display_hand(self, hand, is_dealer=False, hide_first_card=False):
        if is_dealer:
            print("Dealer's hand:")
            if hide_first_card:
                print("[Hidden Card]")
                for card in hand[1:]:
                    print(f"{card[0]} of {card[1]}")

            else:
                for card in hand:
                    print(f"{card[0]} of {card[1]}")
        else:
            print("Your hand:")
            for card in hand:
                print(f"{card[0]} of {card[1]}")

    def play_round(self):
        # Deal initial hands
        self.deal_card(self.player_hand)
        self.deal_card(self.dealer_hand)
        self.deal_card(self.player_hand)
        self.deal_card(self.dealer_hand)

        self.player_score = self.calculate_hand_score(self.player_hand)
        self.dealer_score = self.calculate_hand_score(self.dealer_hand)

        # Player's turn
        self.display_hand(self.player_hand)
        self.display_hand(self.dealer_hand, is_dealer=True, hide_first_card=True)
        print(f"Your score: {self.player_score}")

        while self.player_score < 21:
            action = input("Hit or Stand? (h/s): ").lower()
            if action == "h":
                card = self.deal_card(self.player_hand)
                self.player_score = self.calculate_hand_score(self.player_hand)
                print(f"You drew {card[0]} of {card[1]}")
                self.display_hand(self.player_hand)
                print(f"Your score: {self.player_score}")
                if self.player_score > 21:
                    print("Bust!")
                    self.game_over = True
                    break
            elif action == "s":
                break
            else:
                print("Invalid input. Please enter 'h' or 's'.")

        if not self.game_over:
            # Dealer's turn
            print("\nDealer's turn:")
            self.display_hand(self.dealer_hand, is_dealer=True)
            print(f"Dealer's score: {self.dealer_score}")

            while self.dealer_score < 17:
                card = self.deal_card(self.dealer_hand)
                self.dealer_score = self.calculate_hand_score(self.dealer_hand)
                print(f"Dealer drew {card[0]} of {card[1]}")
                self.display_hand(self.dealer_hand, is_dealer=True)
                print(f"Dealer's score: {self.dealer_score}")
                if self.dealer_score > 21:
                    print("Dealer busts!")
                    break

            # Determine the winner
            if self.player_score > 21:
                print("You lose!")
            elif self.dealer_score > 21:
                print("You win!")
            elif self.player_score > self.dealer_score:
                print("You win!")
            elif self.player_score < self.dealer_score:
                print("You lose!")
            else:
                print("It's a tie!")

        self.game_over = True

    def reset_game(self):
        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []
        self.player_score = 0
        self.dealer_score = 0
        self.game_over = False

    def play_game(self):
        while True:
            self.reset_game()
            self.play_round()

            play_again = input("Play again? (y/n): ").lower()
            if play_again != "y":
                break

if __name__ == "__main__":
    game = Blackjack()
    game.play_game()