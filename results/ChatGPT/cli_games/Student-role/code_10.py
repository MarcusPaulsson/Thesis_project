import random

class Hammurabi:
    def __init__(self):
        self.year = 1
        self.population = 100
        self.bushels = 2800
        self.land = 100
        self.plague = False
        self.famine = False

    def display_status(self):
        print(f"Year: {self.year}")
        print(f"Population: {self.population}")
        print(f"Bushels: {self.bushels}")
        print(f"Land: {self.land} acres")
        print()

    def simulate_year(self):
        self.year += 1
        self.check_events()
        self.harvest()
        self.check_population()

    def check_events(self):
        event = random.choice(['none', 'plague', 'famine'])
        if event == 'plague':
            self.plague = True
            self.population -= self.population // 2
            print("A plague has struck! Half of the population has died.")
        elif event == 'famine':
            self.famine = True
            print("There is a famine this year!")

    def harvest(self):
        if self.famine:
            self.bushels -= self.population // 2
            self.famine = False
        bushels_per_acre = random.randint(1, 6)  # Random yield between 1 and 6
        self.bushels += bushels_per_acre * self.land
        print(f"Harvested {bushels_per_acre * self.land} bushels.")

    def check_population(self):
        if self.bushels < self.population:
            print("Not enough food! The population is starving!")
            self.population -= self.population // 4

    def buy_land(self, acres):
        if self.bushels >= acres * 20:
            self.land += acres
            self.bushels -= acres * 20
            print(f"Bought {acres} acres of land.")
        else:
            print("Not enough bushels to buy land.")

    def sell_land(self, acres):
        if self.land >= acres:
            self.land -= acres
            self.bushels += acres * 10
            print(f"Sold {acres} acres of land.")
        else:
            print("Not enough land to sell.")

    def feed_people(self, bushels):
        if self.bushels >= bushels:
            self.bushels -= bushels
            print(f"Fed the people {bushels} bushels.")
        else:
            print("Not enough bushels to feed the people.")

    def main(self):
        while self.year <= 10 and self.population > 0:
            self.display_status()
            print("Choose an action:")
            print("1. Buy land")
            print("2. Sell land")
            print("3. Feed people")
            action = input("Enter action number: ")

            if action == '1':
                acres = int(input("Enter acres to buy: "))
                self.buy_land(acres)
            elif action == '2':
                acres = int(input("Enter acres to sell: "))
                self.sell_land(acres)
            elif action == '3':
                bushels = int(input("Enter bushels to feed the people: "))
                self.feed_people(bushels)
            else:
                print("Invalid action.")

            self.simulate_year()

        print("Game over!")
        print(f"You survived for {self.year - 1} years.")

if __name__ == "__main__":
    game = Hammurabi()
    game.main()