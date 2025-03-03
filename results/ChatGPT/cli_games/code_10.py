import random

class Hammurabi:
    def __init__(self):
        self.year = 1
        self.bushels = 100
        self.population = 100
        self.land = 100
        self.plague = False
        self.famine = False
        self.harvest_yield = 3

    def print_status(self):
        print(f"\nYear: {self.year}")
        print(f"Bushels: {self.bushels}")
        print(f"Population: {self.population}")
        print(f"Land: {self.land}")
        print(f"Plague: {'Yes' if self.plague else 'No'}")
        print(f"Famine: {'Yes' if self.famine else 'No'}")

    def plant_crops(self, bushels):
        if bushels > self.bushels:
            print("You don't have enough bushels!")
            return 0
        self.bushels -= bushels
        return bushels

    def harvest(self, planted):
        if planted > self.land:
            print("You can't plant more than the land you have!")
            return 0
        yield_harvest = planted * self.harvest_yield
        self.bushels += yield_harvest
        return yield_harvest

    def handle_population_change(self):
        if self.famine:
            self.population -= int(self.population * 0.2)
        if self.plague:
            self.population -= int(self.population * 0.1)

    def next_year(self):
        self.year += 1
        self.handle_population_change()
        self.check_events()

    def check_events(self):
        if random.random() < 0.1:  # 10% chance of plague
            self.plague = True
        else:
            self.plague = False

        if random.random() < 0.1:  # 10% chance of famine
            self.famine = True
        else:
            self.famine = False

    def play(self):
        while self.year <= 10 and self.population > 0:
            self.print_status()
            planted = int(input("Enter the number of bushels to plant: "))
            bushels_used = self.plant_crops(planted)
            if bushels_used > 0:
                harvest_yield = self.harvest(bushels_used)
                print(f"You harvested {harvest_yield} bushels!")
            self.next_year()

        if self.population <= 0:
            print("Your population has died out. You lose!")
        else:
            print("Game over! You survived 10 years.")

if __name__ == "__main__":
    game = Hammurabi()
    game.play()