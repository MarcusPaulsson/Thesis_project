import random

class HammurabiGame:
    def __init__(self):
        self.year = 1
        self.bushels = 100
        self.population = 100
        self.land = 100
        self.plague_years = 0
        self.harvest_yield = 3
        self.rats = 0
        self.famine_years = 0

    def display_status(self):
        print(f"\nYear: {self.year}")
        print(f"Bushels: {self.bushels}")
        print(f"Population: {self.population}")
        print(f"Land: {self.land}")
        print(f"Plague Years: {self.plague_years}")
        print(f"Rats: {self.rats}")
        print(f"Famine Years: {self.famine_years}\n")

    def harvest(self):
        if self.land > 0:
            yield_harvest = self.land * self.harvest_yield
            self.bushels += yield_harvest
            print(f"You harvested {yield_harvest} bushels.")
        else:
            print("You have no land to harvest.")

    def feed_population(self, bushels_to_feed):
        if bushels_to_feed > self.bushels:
            print("Not enough bushels to feed the population!")
            self.population -= self.population // 10  # Lose 10% of population
        else:
            self.bushels -= bushels_to_feed

    def plant_crops(self, acres):
        if acres > self.bushels:
            print("Not enough bushels to plant crops!")
        else:
            self.bushels -= acres
            self.land += acres
            print(f"You planted {acres} acres of crops.")

    def random_events(self):
        event = random.choice(['plague', 'rats', 'famine', 'none'])
        if event == 'plague':
            self.plague_years += 1
            self.population -= self.population // 2  # Population cut by half
            print("A plague has struck! Half of your population has died.")
        elif event == 'rats':
            self.rats = random.randint(1, 30)
            self.bushels -= self.rats
            if self.bushels < 0:
                self.bushels = 0
            print(f"Rats have eaten {self.rats} bushels!")
        elif event == 'famine':
            self.famine_years += 1
            self.population -= self.population // 5  # Population cut by 20%
            print("A famine has occurred! Your population suffers.")

    def play(self):
        while self.year <= 10 and self.population > 0:
            self.display_status()
            print("Actions: 1) Harvest, 2) Feed population, 3) Plant crops")
            action = input("Choose an action (1/2/3): ")

            if action == '1':
                self.harvest()
            elif action == '2':
                bushels_to_feed = int(input("Enter bushels to feed the population: "))
                self.feed_population(bushels_to_feed)
            elif action == '3':
                acres = int(input("Enter acres to plant: "))
                self.plant_crops(acres)
            else:
                print("Invalid action. Try again.")

            self.random_events()
            self.year += 1

        self.end_game()

    def end_game(self):
        print("\nGame Over")
        if self.population <= 0:
            print("Your civilization has perished.")
        else:
            print("You survived for 10 years. Well done!")

if __name__ == "__main__":
    game = HammurabiGame()
    game.play()