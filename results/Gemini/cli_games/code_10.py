import random

class Hammurabi:
    """
    A class to represent the game Hammurabi.
    """

    def __init__(self):
        """
        Initializes the game with default values.
        """
        self.year = 1
        self.population = 100
        self.grain = 2800
        self.acres = 3000
        self.price_land = 19  # Initial price of land (randomized later)
        self.deaths = 0
        self.starved = 0
        self.harvest = 3
        self.rats_ate = 200
        self.immigrants = 5

    def play_year(self):
        """
        Plays one year of the game.
        """
        print(f"\nYear {self.year}")
        print(f"You are in year {self.year} of your ten-year rule.")
        print(f"In the previous year {self.deaths} people starved to death.")
        print(f"The population is now {self.population}.")
        print(f"You harvested {self.harvest} bushels per acre.")
        print(f"Rats ate {self.rats_ate} bushels.")
        print(f"You now have {self.grain} bushels of grain in storage.")
        print(f"The city owns {self.acres} acres of land.")
        print(f"Land is trading at {self.price_land} bushels per acre.")

        self.ask_actions()
        self.calculate_year_end()

    def ask_actions(self):
        """
        Asks the player for actions to take.
        """
        while True:
            try:
                self.buy_sell = int(input("How many acres do you wish to buy/sell? "))
                if self.buy_sell < 0:  # Selling land
                    if abs(self.buy_sell) > self.acres:
                        print("Hammurabi: Think again. You only own", self.acres, "acres.")
                        continue
                elif self.buy_sell > 0:  # Buying land
                    if self.buy_sell * self.price_land > self.grain:
                        print("Hammurabi: Think again. You only have", self.grain, "bushels of grain.")
                        continue
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

        while True:
            try:
                self.feed = int(input("How many bushels do you wish to feed your people? "))
                if self.feed > self.grain:
                    print("Hammurabi: Think again. You only have", self.grain, "bushels of grain.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

        while True:
            try:
                self.plant = int(input("How many acres do you wish to plant with grain? "))
                if self.plant > self.acres:
                    print("Hammurabi: Think again. You only have", self.acres, "acres.")
                    continue
                if self.plant > self.grain:
                    print("Hammurabi: Think again. You only have", self.grain, "bushels of grain.")
                    continue
                if self.plant > self.population * 10:
                    print("Hammurabi: Think again. You only have", self.population, "people to tend the fields.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

    def calculate_year_end(self):
        """
        Calculates the results of the year.
        """

        # Buy/Sell Land
        self.acres += self.buy_sell  # Acres owned are updated
        self.grain -= self.buy_sell * self.price_land # Grain is updated

        # Calculate starvation
        self.starved = 0
        if self.feed < self.population * 20:
            self.starved = int((self.population * 20 - self.feed) / 20)
            if self.starved > self.population:
                self.starved = self.population
            self.population -= self.starved

        # Calculate immigration
        self.immigrants = 0
        if self.starved == 0:
            self.immigrants = int(random.randint(0, 5) * (20 * self.acres + self.grain) / self.population / 100)
        self.population += self.immigrants

        # Calculate harvest
        self.harvest = random.randint(1, 6)  # Random harvest yield
        self.grain += self.plant * self.harvest
        
        # Rats attack
        self.rats_ate = 0
        if random.randint(0, 1) == 0:
            self.rats_ate = int(self.grain * random.uniform(0.1, 0.3))
            self.grain -= self.rats_ate

        # Calculate new grain amount
        self.grain -= self.feed
        self.grain -= self.plant

        # Plague
        self.deaths = 0
        if random.randint(0, 15) == 0:
            self.deaths = int(self.population / 2)
            self.population -= self.deaths
            print("A horrible plague struck! Half the people died.")

        # Calculate new land price
        self.price_land = random.randint(17, 23)

    def is_game_over(self):
        """
        Checks if the game is over.
        """
        if self.year > 10:
            return True
        if self.population <= 0:
            print("Due to your poor leadership, everyone has died.  The game is over.")
            return True
        if self.starved > (0.45 * self.population):
            print("You starved more than 45% of the population! You are immediately deposed by force!")
            return True
        return False

    def calculate_score(self):
        """
        Calculates the player's score.
        """
        acres_per_person = self.acres / self.population
        print("\nFinal Report:")
        print(f"You ruled for {self.year - 1} years.")
        print(f"You ended with {self.population} people.")
        print(f"You owned {self.acres} acres of land.")
        print(f"Acres per person: {acres_per_person:.2f}")

        if acres_per_person > 10:
            print("A fantastic performance!  Well done!")
        elif acres_per_person > 7:
            print("Your performance could have been better.")
        elif acres_per_person > 5:
            print("Your performance was adequate.")
        else:
            print("Your performance was poor.  You are banished from the kingdom.")

    def play_game(self):
        """
        Plays the entire game.
        """
        print("Welcome to the ancient Sumerian city state game of Hammurabi!\n")
        print("Try your hand at governing a city state for ten years.")

        while not self.is_game_over():
            self.play_year()
            self.year += 1

        if self.year > 10:
            self.calculate_score()

if __name__ == "__main__":
    game = Hammurabi()
    game.play_game()