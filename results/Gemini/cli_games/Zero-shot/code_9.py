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
            if rank in ["Jack", "Queen", "King"]:
                score += 10
            elif rank == "Ace":
                score += 11
                ace_count += 1
            else:
                score += int(rank)

        while score > 21 and ace_count > 0:
            score -= 10
            ace_count -= 1

        return score

    def display_hand(self, hand, is_dealer=False, hide_first_card=False):
        if is_dealer:
            print("Dealer's hand:")
            if hide_first_card:
                print("[Hidden Card]")
                for card in hand[1:]:
                    print(f" {card[0]} of {card[1]}")
            else:
                for card in hand:
                    print(f" {card[0]} of {card[1]}")
            if not hide_first_card:
                print(f"Dealer's score: {self.dealer_score}")
        else:
            print("Your hand:")
            for card in hand:
                print(f" {card[0]} of {card[1]}")
            print(f"Your score: {self.player_score}")

    def play_round(self):
        # Deal initial hands
        for _ in range(2):
            self.deal_card(self.player_hand)
            self.deal_card(self.dealer_hand)

        self.player_score = self.calculate_hand_score(self.player_hand)
        self.dealer_score = self.calculate_hand_score(self.dealer_hand)

        # Player's turn
        self.display_hand(self.player_hand)
        self.display_hand(self.dealer_hand, is_dealer=True, hide_first_card=True)


        while self.player_score < 21:
            action = input("Hit or Stand? (h/s): ").lower()
            if action == 'h':
                self.deal_card(self.player_hand)
                self.player_score = self.calculate_hand_score(self.player_hand)
                self.display_hand(self.player_hand)

                if self.player_score > 21:
                    print("Bust!")
                    self.game_over = True
                    return
            elif action == 's':
                break
            else:
                print("Invalid input. Please enter 'h' or 's'.")

        # Dealer's turn
        if not self.game_over:
            print("\nDealer's turn:")
            self.display_hand(self.dealer_hand, is_dealer=True)

            while self.dealer_score < 17:
                self.deal_card(self.dealer_hand)
                self.dealer_score = self.calculate_hand_score(self.dealer_hand)
                print("Dealer hits.")
                self.display_hand(self.dealer_hand, is_dealer=True)
                if self.dealer_score > 21:
                    print("Dealer busts!")
                    break

        # Determine the winner
        self.determine_winner()

    def determine_winner(self):
        print("\n--- Final Results ---")
        self.display_hand(self.player_hand)
        self.display_hand(self.dealer_hand, is_dealer=True)

        if self.player_score > 21:
            print("You lose!")
        elif self.dealer_score > 21:
            print("You win!")
        elif self.player_score > self.dealer_score:
            print("You win!")
        elif self.dealer_score > self.player_score:
            print("You lose!")
        else:
            print("It's a tie!")

    def play_again(self):
        while True:
            answer = input("Play again? (y/n): ").lower()
            if answer == 'y':
                self.__init__()  # Reset the game
                return True
            elif answer == 'n':
                return False
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

    def start_game(self):
        print("Welcome to Blackjack!")
        while True:
            self.play_round()
            if not self.play_again():
                print("Thanks for playing!")
                break


if __name__ == "__main__":
    game = Blackjack()
    game.start_game()