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
        self.grain = 2800
        self.land = 1000
        self.price_of_land = 19  # Initial price per acre
        self.deaths = 0
        self.starved = 0
        self.harvest = 3  # Initial average harvest yield per acre
        self.rats_ate = 0


    def play_year(self):
        """
        Plays one year of the game.
        """

        print(f"\nYear {self.year}")
        print(f"You are in year {self.year} of your ten-year rule.")
        print(f"Population is now {self.population}")
        print(f"You own {self.land} acres of land.")
        print(f"You have {self.grain} bushels of grain in storage.")
        print(f"Land is trading at {self.price_of_land} bushels per acre.")

        # Ask the player for their decisions
        acres_to_buy = self.ask_to_buy_land()
        acres_to_sell = self.ask_to_sell_land()
        grain_to_feed = self.ask_to_feed_people()
        acres_to_plant = self.ask_to_plant_land()

        # Handle the consequences of the decisions
        self.handle_land_transactions(acres_to_buy, acres_to_sell)
        self.handle_feeding(grain_to_feed)
        self.handle_planting(acres_to_plant)
        self.handle_harvest()
        self.handle_rats()
        self.handle_starvation()
        self.handle_population_growth()
        self.handle_new_price_of_land()

        # Update the year
        self.year += 1


    def ask_to_buy_land(self):
        """
        Asks the player how many acres of land they want to buy.
        """
        while True:
            try:
                acres = int(input("How many acres do you wish to buy? "))
                if acres < 0:
                    print("Please enter a non-negative number.")
                elif acres * self.price_of_land > self.grain:
                    print("You do not have enough grain to buy that much land.")
                else:
                    return acres
            except ValueError:
                print("Invalid input. Please enter a number.")

    def ask_to_sell_land(self):
        """
        Asks the player how many acres of land they want to sell.
        """
        while True:
            try:
                acres = int(input("How many acres do you wish to sell? "))
                if acres < 0:
                    print("Please enter a non-negative number.")
                elif acres > self.land:
                    print("You do not have that much land to sell.")
                else:
                    return acres
            except ValueError:
                print("Invalid input. Please enter a number.")

    def ask_to_feed_people(self):
        """
        Asks the player how much grain they want to use to feed their people.
        """
        while True:
            try:
                grain = int(input("How many bushels do you wish to feed your people? "))
                if grain < 0:
                    print("Please enter a non-negative number.")
                elif grain > self.grain:
                    print("You do not have that much grain.")
                else:
                    return grain
            except ValueError:
                print("Invalid input. Please enter a number.")

    def ask_to_plant_land(self):
        """
        Asks the player how many acres of land they want to plant.
        """
        while True:
            try:
                acres = int(input("How many acres do you wish to plant with grain? "))
                if acres < 0:
                    print("Please enter a non-negative number.")
                elif acres > self.land:
                    print("You do not have that much land.")
                elif acres * 2 > self.grain:
                    print("You do not have enough grain to plant that much land (2 bushels per acre required).")
                elif acres > self.population * 10:
                    print("You do not have enough people to plant that much land (each person can plant 10 acres).")
                else:
                    return acres
            except ValueError:
                print("Invalid input. Please enter a number.")


    def handle_land_transactions(self, acres_to_buy, acres_to_sell):
        """
        Handles the buying and selling of land.
        """
        self.grain -= acres_to_buy * self.price_of_land
        self.grain += acres_to_sell * self.price_of_land
        self.land += acres_to_buy - acres_to_sell


    def handle_feeding(self, grain_to_feed):
        """
        Handles the feeding of the population.
        """
        self.grain -= grain_to_feed


    def handle_planting(self, acres_to_plant):
        """
        Handles the planting of land.
        """
        self.planted_acres = acres_to_plant


    def handle_harvest(self):
        """
        Handles the harvest.
        """
        self.harvest = random.randint(1, 6)  # Random harvest yield
        grain_harvested = self.planted_acres * self.harvest
        self.grain += grain_harvested
        print(f"Harvest was {self.harvest} bushels per acre.  You harvested {grain_harvested} bushels.")


    def handle_rats(self):
        """
        Handles the rat infestation.
        """
        rat_infestation = random.randint(0, 100)
        if rat_infestation <= 40:  # 40% chance of rat infestation
            self.rats_ate = int(self.grain * random.uniform(0.1, 0.3))  # Rats eat 10-30% of the grain
            self.grain -= self.rats_ate
            print(f"Rats ate {self.rats_ate} bushels of grain!")
        else:
            self.rats_ate = 0


    def handle_starvation(self):
        """
        Handles starvation and its consequences.
        """
        grain_needed = self.population * 20 # 20 bushels of grain per person
        if self.grain < grain_needed:
            starved = self.population - int(self.grain / 20)
            if starved < 0 : starved = 0
            self.starved = starved
            self.population -= starved
            print(f"{starved} people starved this year.")

            if self.population <= 0:
                print("You have starved all your people! Game Over.")
                self.game_over = True
                return

            if starved > self.population * 0.5:
                print("Due to your poor management, the people have revolted! Game Over.")
                self.game_over = True
                return
        else:
            self.starved = 0
            print("No one starved this year.")


    def handle_population_growth(self):
        """
        Handles population growth.
        """
        if self.starved == 0:
            growth = int(self.population * random.uniform(0.0, 0.15))  # 0-15% growth
            self.population += growth
            print(f"The population grew by {growth} people.")
        else:
            print("The population did not grow this year due to starvation.")


    def handle_new_price_of_land(self):
        """
        Handles the change in the price of land.
        """
        self.price_of_land = random.randint(17, 25)


    def is_game_over(self):
        """
        Checks if the game is over.
        """
        if self.year > 10 or self.game_over:
            return True
        else:
            return False

    def print_final_score(self):
        """
        Prints the final score based on performance.
        """
        acres_per_person = self.land / self.population
        print("\nFinal Report:")
        print(f"You ruled for 10 years.")
        print(f"At the end of your rule, you had {self.population} people.")
        print(f"You owned {self.land} acres of land.")
        print(f"That's {acres_per_person:.2f} acres per person.")

        if acres_per_person > 10:
            print("A fantastic performance! Well done, Hammurabi!")
        elif acres_per_person > 7:
            print("A good performance. You could have done better.")
        elif acres_per_person > 4:
            print("An average performance. Not great, not terrible.")
        else:
            print("A poor performance. You were a terrible ruler!")

    def play_game(self):
        """
        Plays the entire game.
        """
        self.game_over = False
        print("Welcome to Hammurabi!")

        while not self.is_game_over():
            self.play_year()

        if self.game_over and self.population > 0 :
            print("Game Over.")
        elif self.year > 10:
            self.print_final_score()




# Create an instance of the game and play it
if __name__ == "__main__":
    game = Hammurabi()
    game.play_game()