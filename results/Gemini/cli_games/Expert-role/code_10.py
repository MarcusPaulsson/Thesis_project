import random

class Hammurabi:
    """
    A class representing the Hammurabi game.
    """

    def __init__(self):
        """
        Initializes the game state.
        """
        self.year = 1
        self.population = 100
        self.grain_stores = 2800
        self.acres_owned = 1000
        self.price_per_acre = 19  #initial price
        self.starved = 0
        self.plague_deaths = 0

    def play_year(self):
        """
        Plays one year of the game.
        """
        print(f"\nYear {self.year}")
        print(f"You are in year {self.year} of your ten-year rule.")
        print(f"In the previous year {self.starved} people starved to death.")
        if self.plague_deaths > 0:
            print(f"The plague killed {self.plague_deaths} people.")
        print(f"The population is now {self.population}.")
        print(f"You own {self.acres_owned} acres of land.")
        print(f"You harvested {self.grain_stores} bushels of grain.")
        print(f"Land is trading at {self.price_per_acre} bushels per acre.")

        self.handle_trading()
        self.handle_feeding()
        self.handle_planting()
        self.handle_harvest()
        self.handle_plague()
        self.handle_population()
        self.handle_rats()
        self.handle_land_price()

        self.year += 1

    def handle_trading(self):
        """
        Handles buying and selling land.
        """
        while True:
            try:
                acres_to_buy = int(input("How many acres do you wish to buy? "))
                if acres_to_buy < 0:
                    print("You cannot buy a negative number of acres.")
                    continue
                if acres_to_buy * self.price_per_acre > self.grain_stores:
                    print("O Hammurabi, we have not enough grain!")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        while True:
            try:
                acres_to_sell = int(input("How many acres do you wish to sell? "))
                if acres_to_sell < 0:
                    print("You cannot sell a negative number of acres.")
                    continue
                if acres_to_sell > self.acres_owned:
                    print("O Hammurabi, you do not own that much land!")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        self.acres_owned += acres_to_buy - acres_to_sell
        self.grain_stores -= acres_to_buy * self.price_per_acre
        self.grain_stores += acres_to_sell * self.price_per_acre

    def handle_feeding(self):
        """
        Handles feeding the population.
        """
        while True:
            try:
                grain_to_feed = int(input("How many bushels do you wish to feed your people? "))
                if grain_to_feed < 0:
                    print("You cannot feed a negative amount of grain.")
                    continue
                if grain_to_feed > self.grain_stores:
                    print("O Hammurabi, we have not enough grain!")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        self.grain_stores -= grain_to_feed
        grain_per_person = grain_to_feed / self.population

        if grain_per_person < 20:
            starved = int(self.population * (20 - grain_per_person) / 20)
            self.starved = starved
            self.population -= starved
            print(f"{starved} people have starved.")
            if self.population <= 0:
                print("O Hammurabi, you have starved all your people. Your rule is over!")
                exit()
        else:
            self.starved = 0

    def handle_planting(self):
        """
        Handles planting grain.
        """
        while True:
            try:
                acres_to_plant = int(input("How many acres do you wish to plant with grain? "))
                if acres_to_plant < 0:
                    print("You cannot plant a negative number of acres.")
                    continue
                if acres_to_plant > self.acres_owned:
                    print("O Hammurabi, you do not own that much land!")
                    continue
                if acres_to_plant > self.grain_stores / 1:  # 1 bushel per acre
                    print("O Hammurabi, we have not enough grain!")
                    continue
                if acres_to_plant > self.population * 10: #10 acres per person
                    print("O Hammurabi, we do not have enough people to tend that land!")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        self.grain_stores -= acres_to_plant
        self.acres_planted = acres_to_plant

    def handle_harvest(self):
        """
        Handles the harvest.
        """
        harvest = int(random.randint(1, 5) * self.acres_planted)
        self.grain_stores += harvest
        print(f"You harvested {harvest} bushels of grain.")

    def handle_plague(self):
        """
        Handles the possibility of plague.
        """
        if random.randint(1, 10) == 1:
            self.plague_deaths = int(self.population / 2)
            self.population -= self.plague_deaths
            print("A horrible plague has struck! Half the people have died.")
        else:
            self.plague_deaths = 0

    def handle_population(self):
        """
        Handles population growth.
        """
        self.population += int(self.population * (random.randint(5, 15) / 100))
        if self.population < 0:
            self.population = 0

    def handle_rats(self):
        """
        Handles rat infestations.
        """
        if random.randint(1, 10) <= 3:
            rats_ate = int(self.grain_stores * random.randint(10, 30) / 100)
            self.grain_stores -= rats_ate
            print(f"Rats ate {rats_ate} bushels of grain!")

    def handle_land_price(self):
        """
        Handles the fluctuation of land prices.
        """
        self.price_per_acre = random.randint(17, 23)

    def game_over(self):
        """
        Checks if the game is over.
        """
        if self.year > 10:
            print("\nYour reign is over!")
            print(f"In your ten-year rule, you starved {self.starved} people on average per year.")
            acres_per_person = self.acres_owned / self.population
            print(f"You ended with {acres_per_person} acres per person.")

            if self.starved > (0.45 * self.population):
                print("Due to this extreme negligence, you have not only been impeached and thrown out of office but have also been declared 'National Fickle Head'!")
            elif acres_per_person < 7:
                print("Your heavy handed taxation and poor management have left everyone destitute. You have been impeached and thrown out of office!")
            elif acres_per_person < 9:
                print("Your performance could have been better. Many people have fled to other kingdoms.")
            elif acres_per_person < 10:
                print("Your performance was adequate, but not great.")
            else:
                print("A fantastic job! You are known throughout the land as a wise and benevolent ruler!")
            return True
        return False

    def play_game(self):
        """
        Plays the entire game.
        """
        print("Welcome to Hammurabi!")
        while not self.game_over():
            self.play_year()

if __name__ == "__main__":
    game = Hammurabi()
    game.play_game()