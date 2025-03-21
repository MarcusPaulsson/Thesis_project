import random

class Hammurabi:
    def __init__(self):
        self.year = 1
        self.population = 100
        self.grain = 2800
        self.land = 100
        self.plague_years = 0
        self.harvest_yield = 3
        self.deaths = 0

    def print_status(self):
        print(f"Year: {self.year}")
        print(f"Population: {self.population}")
        print(f"Grain: {self.grain} bushels")
        print(f"Land: {self.land} acres")
        print(f"Plague Years: {self.plague_years}")

    def get_input(self, prompt, valid_options=None):
        while True:
            response = input(prompt).strip()
            if valid_options and response not in valid_options:
                print(f"Invalid input. Please choose from {valid_options}.")
            else:
                return response

    def harvest(self):
        yield_bushels = self.land * self.harvest_yield
        self.grain += yield_bushels
        print(f"You harvested {yield_bushels} bushels of grain.")

    def manage_population(self):
        if self.plague_years > 0:
            deaths = random.randint(0, self.population // 2)
            self.deaths += deaths
            self.population -= deaths
            self.plague_years -= 1
            print(f"The plague has taken {deaths} people.")
        else:
            births = self.population // 10
            self.population += births
            print(f"{births} people were born.")

    def trade_grain(self):
        while True:
            bushels = int(self.get_input("How many bushels of grain will you trade? "))
            if bushels < 0 or bushels > self.grain:
                print("You cannot trade more grain than you have.")
            else:
                self.grain -= bushels
                self.grain += bushels * 2  # Assume a 2 for 1 trade ratio
                print(f"You traded {bushels} bushels and now have {self.grain} bushels.")
                break

    def plant_crops(self):
        while True:
            acres = int(self.get_input("How many acres will you plant? "))
            if acres < 0 or acres > self.land:
                print("You cannot plant more acres than you own.")
            else:
                self.land -= acres
                self.grain -= acres  # Assume 1 bushel per acre to plant
                print(f"You planted crops on {acres} acres.")
                break

    def next_year(self):
        self.year += 1
        self.harvest()
        self.manage_population()
        if random.random() < 0.1:  # 10% chance of plague
            self.plague_years = random.randint(1, 3)
            print("A plague has struck the city!")

    def play(self):
        while self.year <= 10 and self.population > 0:
            self.print_status()
            self.plant_crops()
            self.trade_grain()
            self.next_year()

        if self.population <= 0:
            print("Your civilization has collapsed!")
        else:
            print("You have survived for 10 years!")

if __name__ == "__main__":
    game = Hammurabi()
    game.play()