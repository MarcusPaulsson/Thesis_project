import random

class Hammurabi:
    def __init__(self):
        self.year = 1
        self.population = 100
        self.land = 1000
        self.bushels = 2800
        self.harvest = 3
        self.plague = False
        self.starving = False
        self.land_price = 20
        self.max_years = 10

    def print_status(self):
        print(f"\nYear: {self.year}")
        print(f"Population: {self.population}")
        print(f"Land: {self.land} acres")
        print(f"Bushels of grain: {self.bushels}")
        print(f"Harvest per acre: {self.harvest} bushels")
        print(f"Plague: {'Yes' if self.plague else 'No'}")
        print(f"Starving: {'Yes' if self.starving else 'No'}")

    def calculate_harvest(self):
        return self.land * self.harvest

    def next_year(self):
        self.year += 1
        self.harvest = random.randint(1, 6)
        self.bushels += self.calculate_harvest()
        self.handle_plague()
        self.handle_starvation()
        self.check_end_game()

    def handle_plague(self):
        if random.random() < 0.2:
            self.plague = True
            lost_population = int(self.population * 0.5)
            self.population -= lost_population
            print(f"A plague has struck! You lost {lost_population} people.")

    def handle_starvation(self):
        if self.bushels < self.population:
            self.starving = True
            lost_population = self.population - self.bushels
            self.population -= lost_population
            self.bushels = 0
            print(f"Starvation has occurred! You lost {lost_population} people.")

    def check_end_game(self):
        if self.population <= 0 or self.year > self.max_years:
            self.end_game()

    def end_game(self):
        print("\nGame Over!")
        if self.population <= 0:
            print("Your population has died out.")
        else:
            print("You have ruled for 10 years.")
        exit()

    def buy_land(self, acres):
        cost = acres * self.land_price
        if cost > self.bushels:
            print("You do not have enough bushels to buy that much land.")
            return
        self.land += acres
        self.bushels -= cost
        print(f"You bought {acres} acres of land.")

    def sell_land(self, acres):
        if acres > self.land:
            print("You do not own that much land.")
            return
        self.land -= acres
        self.bushels += acres * self.land_price
        print(f"You sold {acres} acres of land.")

    def feed_population(self, bushels):
        if bushels > self.bushels:
            print("You do not have enough bushels to feed that many people.")
            return
        self.bushels -= bushels
        self.starving = False
        print(f"You fed the population {bushels} bushels of grain.")

    def play(self):
        while True:
            self.print_status()
            print("\nOptions:")
            print("1. Buy land")
            print("2. Sell land")
            print("3. Feed population")
            print("4. End year")

            choice = input("Choose an option (1-4): ")

            if choice == '1':
                acres = int(input("How many acres do you want to buy? "))
                self.buy_land(acres)
            elif choice == '2':
                acres = int(input("How many acres do you want to sell? "))
                self.sell_land(acres)
            elif choice == '3':
                bushels = int(input("How many bushels do you want to feed the population? "))
                self.feed_population(bushels)
            elif choice == '4':
                self.next_year()
            else:
                print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    game = Hammurabi()
    game.play()