import random

class Hammurabi:
    def __init__(self):
        self.year = 1960
        self.population = 100
        self.bushels = 2800
        self.land = 100
        self.plague_years = 0
        self.harvest_yield = 3
        self.max_years = 10
        self.game_over = False

    def play(self):
        while not self.game_over:
            self.display_status()
            self.year += 1
            self.take_turn()
            self.check_game_over()

    def display_status(self):
        print(f"\nYear: {self.year}")
        print(f"Population: {self.population}")
        print(f"Bushels: {self.bushels}")
        print(f"Land: {self.land} acres")

    def take_turn(self):
        self.ask_land()
        self.ask_food()
        self.harvest()
        self.random_events()
        self.update_population()

    def ask_land(self):
        while True:
            try:
                land = int(input(f"How many acres of land do you want to buy/sell? (0 to {self.bushels // 20}): "))
                if -self.land <= land <= self.bushels // 20:
                    self.land += land
                    self.bushels -= land * 20
                    break
                else:
                    print("Invalid amount.")
            except ValueError:
                print("Please enter a valid number.")

    def ask_food(self):
        while True:
            try:
                food = int(input(f"How many bushels do you want to feed your people? (0 to {self.bushels}): "))
                if 0 <= food <= self.bushels:
                    self.bushels -= food
                    break
                else:
                    print("Invalid amount.")
            except ValueError:
                print("Please enter a valid number.")

    def harvest(self):
        harvested = self.land * self.harvest_yield
        self.bushels += harvested
        print(f"You harvested {harvested} bushels.")

    def random_events(self):
        if random.random() < 0.15:
            self.plague_years += 1
            lost_population = self.population // 2
            self.population -= lost_population
            print(f"A plague has struck! You lost half your population: {lost_population} people.")

    def update_population(self):
        if self.bushels < self.population:
            starved = self.population - self.bushels
            self.population -= starved
            print(f"{starved} people have died from starvation.")
        elif self.bushels > self.population * 20:
            immigrants = (self.bushels - (self.population * 20)) // 20
            self.population += immigrants
            print(f"{immigrants} immigrants have arrived.")

    def check_game_over(self):
        if self.year > self.max_years or self.population <= 0:
            self.game_over = True
            if self.population <= 0:
                print("Your population has perished. Game over!")
            else:
                print("You have completed your 10 years of rule. Game over!")

if __name__ == "__main__":
    game = Hammurabi()
    game.play()