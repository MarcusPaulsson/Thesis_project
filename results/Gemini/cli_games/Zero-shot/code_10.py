import random

class Hammurabi:
    """
    A class to represent the game Hammurabi.
    """

    def __init__(self):
        """
        Initializes the game state.
        """
        self.year = 1
        self.population = 100
        self.grain = 2800
        self.acres = 1000
        self.harvest = 3  # Initial harvest rate
        self.rats_ate = 0
        self.people_starved = 0
        self.new_arrivals = 0
        self.price_of_land = 19 + random.randint(-5, 5)  # Initial price of land

    def play_year(self):
        """
        Plays one year of the game.
        """
        print(f"\nYear {self.year}")
        print(f"You are in year {self.year} of your ten-year rule.")
        print(f"Population is now {self.population}")
        print(f"You harvested {self.harvest} bushels per acre.")
        print(f"Rats ate {self.rats_ate} bushels.")
        print(f"You now have {self.grain} bushels in store.")
        print(f"Land is selling for {self.price_of_land} bushels per acre.")

        self.ask_questions()
        self.do_plague()
        self.do_harvest()
        self.do_rats()
        self.do_starvation()
        self.do_migration()
        self.update_land_price()

        self.year += 1

    def ask_questions(self):
        """
        Asks the player for decisions on land, planting, and feeding.
        """
        while True:
            try:
                self.buy_sell = int(input("How many acres do you wish to buy or sell (+/- acres)? "))
                if self.grain < -self.buy_sell * self.price_of_land:
                    print("O great Hammurabi, we do not have enough grain.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")

        while True:
            try:
                self.grain_to_feed = int(input("How many bushels do you wish to feed your people? "))
                if self.grain_to_feed > self.grain:
                    print("O great Hammurabi, we do not have enough grain.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")

        while True:
            try:
                self.acres_to_plant = int(input("How many acres do you wish to plant with seed? "))
                if self.acres_to_plant > self.acres:
                    print("O great Hammurabi, we do not have enough land.")
                elif self.acres_to_plant > self.grain:
                    print("O great Hammurabi, we do not have enough grain.")
                elif self.acres_to_plant > self.population * 10:
                    print("O great Hammurabi, we do not have enough people to tend the fields.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")

    def do_plague(self):
        """
        Simulates a plague that might kill a portion of the population.
        """
        if random.randint(1, 100) <= 15:
            deaths = int(self.population / 2)
            self.population -= deaths
            print(f"A horrible plague struck! Half the people died. {deaths} died.")

    def do_harvest(self):
        """
        Calculates the harvest for the year.
        """
        self.acres += self.buy_sell
        self.grain += -self.buy_sell * self.price_of_land

        self.grain += -self.grain_to_feed

        self.grain += -self.acres_to_plant

        self.harvest = random.randint(1, 8)
        self.grain += self.acres_to_plant * self.harvest

    def do_rats(self):
        """
        Simulates rats eating a portion of the grain.
        """
        self.rats_ate = 0
        if random.randint(1, 100) <= 40:
            self.rats_ate = int(self.grain * random.uniform(0.1, 0.3))
            self.grain -= self.rats_ate
            print(f"Rats ate {self.rats_ate} bushels of grain.")

    def do_starvation(self):
        """
        Calculates starvation and its effects on the population.
        """
        self.people_starved = 0
        if self.grain_to_feed / self.population < 20:
            self.people_starved = int(self.population - (self.grain_to_feed / 20))
            if self.people_starved < 0:
                self.people_starved = 0
            self.population -= self.people_starved
            print(f"{self.people_starved} people starved.")

            if self.population <= 0:
                print("O great Hammurabi, you have killed everyone!")
                return False
        return True

    def do_migration(self):
        """
        Calculates immigration based on the state of the kingdom.
        """
        self.new_arrivals = int((10 * self.acres + self.grain) / self.population / 20 + 1)
        self.population += self.new_arrivals
        print(f"{self.new_arrivals} people came to the city.")

    def update_land_price(self):
        """
        Updates the price of land for the next year.
        """
        self.price_of_land = 19 + random.randint(-5, 5)

    def game_over(self):
        """
        Checks if the game is over and displays the final stats.
        """
        if self.year > 10:
            print("\nYour reign has ended.")
            print(f"Final population: {self.population}")
            print(f"Acres of land owned: {self.acres}")
            print(f"Grain in store: {self.grain}")
            starved_percentage = (sum(year.people_starved for year in self.years_history) / sum(year.population for year in self.years_history)) * 100 if self.years_history else 0.0
            print(f"Starved percentage: {starved_percentage:.2f}%")
            if starved_percentage > 10:
                print("Due to this extreme mismanagement, you have not only been impeached but have also been declared National Fool!!")
            else:
                print("A generally positive outcome, you may be able to rule again.")
            return True
        return False

    def play(self):
        """
        Plays the game for ten years.
        """
        self.years_history = []
        print("Welcome to Hammurabi!")
        while not self.game_over():
            year_data = Hammurabi()
            year_data.year = self.year
            year_data.population = self.population
            year_data.grain = self.grain
            year_data.acres = self.acres
            year_data.harvest = self.harvest
            year_data.rats_ate = self.rats_ate
            year_data.people_starved = self.people_starved
            year_data.new_arrivals = self.new_arrivals
            year_data.price_of_land = self.price_of_land
            
            if not self.play_year():
                return
            
            self.years_history.append(year_data)


if __name__ == "__main__":
    game = Hammurabi()
    game.play()