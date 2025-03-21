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
        self.bushels_per_acre = 3  # Initial yield
        self.deaths = 0
        self.starved = 0
        self.immigrants = 0
        self.plague = False

    def play_year(self):
        """
        Plays one year of the game.
        """
        self.print_status()

        # Plague check
        if random.randint(1, 15) == 1:
            self.plague = True
            print("\nA terrible plague has struck the city!")
            death_toll = int(self.population / 2)
            self.population -= death_toll
            self.deaths += death_toll
            print(f"{death_toll} people have died from the plague.")
        else:
            self.plague = False

        # Ask the player how many acres to buy/sell
        acres_to_buy = self.get_acres_to_buy()
        if acres_to_buy is None:
            return False  # Player quit

        # Ask the player how much grain to feed the people
        grain_to_feed = self.get_grain_to_feed()
        if grain_to_feed is None:
            return False  # Player quit

        # Ask the player how many acres to plant
        acres_to_plant = self.get_acres_to_plant()
        if acres_to_plant is None:
            return False  # Player quit

        # Calculate the outcome of the year
        self.calculate_outcome(acres_to_buy, grain_to_feed, acres_to_plant)
        return True

    def print_status(self):
        """
        Prints the current status of the game.
        """
        print(f"\nYear {self.year}")
        print(f"You are in year {self.year} of your ten-year rule.")
        print(f"In the previous year {self.deaths} people starved to death.")
        print(f"{self.immigrants} people entered the city.")
        print(f"The population is now {self.population}.")
        print(f"You own {self.acres_owned} acres of land.")
        print(f"You harvested {self.bushels_per_acre} bushels per acre.")
        print(f"Rats ate {self.calculate_rat_damage()} bushels of grain.")
        print(f"Grain stores are {self.grain_stores} bushels.")
        print(f"Land is trading at {self.calculate_land_price()} bushels per acre.")

    def get_acres_to_buy(self):
        """
        Asks the player how many acres to buy or sell.
        """
        while True:
            try:
                acres_to_buy = input("How many acres do you wish to buy/sell (enter a negative number to sell)? ")
                if acres_to_buy.lower() == 'quit':
                    return None
                acres_to_buy = int(acres_to_buy)

                if acres_to_buy > 0:  # Buying
                    if acres_to_buy * self.calculate_land_price() > self.grain_stores:
                        print("O Great Hammurabi, you do not have enough grain to buy that much land.")
                    else:
                        return acres_to_buy
                elif acres_to_buy < 0:  # Selling
                    if abs(acres_to_buy) > self.acres_owned:
                        print("O Great Hammurabi, you do not have that much land to sell.")
                    else:
                        return acres_to_buy
                else:
                    return 0
            except ValueError:
                print("Invalid input. Please enter a number or 'quit'.")

    def get_grain_to_feed(self):
        """
        Asks the player how much grain to feed the people.
        """
        while True:
            try:
                grain_to_feed = input("How much grain do you wish to feed your people? ")
                if grain_to_feed.lower() == 'quit':
                    return None
                grain_to_feed = int(grain_to_feed)

                if grain_to_feed > self.grain_stores:
                    print("O Great Hammurabi, you do not have that much grain.")
                elif grain_to_feed < 0:
                    print("O Great Hammurabi, you cannot feed a negative amount of grain.")
                else:
                    return grain_to_feed
            except ValueError:
                print("Invalid input. Please enter a number or 'quit'.")

    def get_acres_to_plant(self):
        """
        Asks the player how many acres to plant.
        """
        while True:
            try:
                acres_to_plant = input("How many acres do you wish to plant with grain? ")
                if acres_to_plant.lower() == 'quit':
                    return None
                acres_to_plant = int(acres_to_plant)

                if acres_to_plant > self.acres_owned:
                    print("O Great Hammurabi, you do not have that much land.")
                elif acres_to_plant * 2 > self.grain_stores:
                    print("O Great Hammurabi, you do not have enough grain to plant that much land.")
                elif acres_to_plant < 0:
                    print("O Great Hammurabi, you cannot plant a negative amount of land.")
                else:
                    return acres_to_plant
            except ValueError:
                print("Invalid input. Please enter a number or 'quit'.")

    def calculate_outcome(self, acres_to_buy, grain_to_feed, acres_to_plant):
        """
        Calculates the outcome of the year based on the player's decisions.
        """
        # Buy/Sell Land
        land_price = self.calculate_land_price()
        self.acres_owned += acres_to_buy
        self.grain_stores -= acres_to_buy * land_price

        # Feed the people
        self.grain_stores -= grain_to_feed

        # Calculate starvation
        food_needed = self.population * 20  # Each person needs 20 bushels
        if grain_to_feed < food_needed:
            starved = (food_needed - grain_to_feed) // 20
            if starved > self.population:
                starved = self.population
            self.starved = starved
            self.deaths = starved
            self.population -= starved
            print(f"{starved} people starved this year.")
        else:
            self.starved = 0
            self.deaths = 0

        # Calculate immigration
        self.immigrants = int((10 * (2 * acres_to_plant / self.population) + (50 * grain_to_feed / self.population) - self.deaths / 2))
        if self.immigrants < 0:
            self.immigrants = 0
        self.population += self.immigrants

        # Plant the crops
        self.grain_stores -= acres_to_plant * 2  # Each acre requires 2 bushels to plant

        # Harvest the crops
        self.bushels_per_acre = random.randint(1, 6)
        harvested = acres_to_plant * self.bushels_per_acre
        self.grain_stores += harvested

        # Rats eat grain
        rat_damage = self.calculate_rat_damage()
        self.grain_stores -= rat_damage
        if self.grain_stores < 0:
            self.grain_stores = 0 # Make sure grain doesn't go negative

        # Check for rebellion
        if self.starved > 0.45 * self.population:
             print("O Great Hammurabi, you have been overthrown by the people due to your poor leadership!")
             exit()

        self.year += 1

    def calculate_land_price(self):
        """
        Calculates the price of land.
        """
        return random.randint(17, 23)

    def calculate_rat_damage(self):
        """
        Calculates the amount of grain eaten by rats.
        """
        if random.randint(1, 10) <= 3:
            rat_damage = int(self.grain_stores * random.uniform(0.1, 0.3))
            print(f"Rats ate {rat_damage} bushels of grain!")
            return rat_damage
        else:
            return 0

    def is_game_over(self):
        """
        Checks if the game is over.
        """
        if self.year > 10:
            return True
        else:
            return False

    def calculate_final_score(self):
        """
        Calculates the player's final score.
        """
        acres_per_person = self.acres_owned / self.population
        print("\nO Great Hammurabi, your rule has come to an end.")
        print(f"You ended with {self.population} people, {self.acres_owned} acres of land, and {self.grain_stores} bushels of grain.")
        print(f"You owned {acres_per_person:.2f} acres per person.")

        if acres_per_person > 10:
            print("A fantastic performance! Well done!")
        elif acres_per_person > 7:
            print("Your performance could have been better, but adequate.")
        elif acres_per_person > 5:
            print("Your performance was barely adequate.")
        else:
            print("Due to this extreme mismanagement, you have not only been impeached and thrown out of office, but you have also been declared 'National Fink'.")


def main():
    """
    Main function to run the game.
    """
    game = Hammurabi()

    print("Welcome to Hammurabi!")
    print("You are the new ruler of the city-state of Sumer.")
    print("You will rule for 10 years.  Make wise decisions, lest you be overthrown.")
    print("You start with 100 people, 2800 bushels of grain, and 1000 acres of land.")

    while not game.is_game_over():
        if not game.play_year():
            print("Game Over.")
            return

    game.calculate_final_score()


if __name__ == "__main__":
    main()