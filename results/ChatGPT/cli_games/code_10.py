import random

class Hammurabi:
    def __init__(self):
        self.year = 1
        self.population = 100
        self.bushels = 2800
        self.land = 100
        self.plague_years = 0
        self.historical_events = {
            'plague': [0.1, 0.3],
            'famine': [0.1, 0.4]
        }

    def print_status(self):
        print(f"Year: {self.year}")
        print(f"Population: {self.population}")
        print(f"Bushels: {self.bushels}")
        print(f"Land: {self.land} acres")
        print()

    def get_input(self, prompt, valid_options=None):
        while True:
            response = input(prompt).strip()
            if valid_options and response not in valid_options:
                print(f"Invalid input. Please choose from {valid_options}.")
            else:
                return response

    def decide(self):
        print("What do you want to do?")
        print("1. Plant bushels")
        print("2. Buy land")
        print("3. Sell land")
        print("4. Feed the people")
        print("5. End year")
        
        decision = self.get_input("Choose an option (1-5): ", ['1', '2', '3', '4', '5'])
        return decision

    def play(self):
        while self.year <= 10:
            self.print_status()
            decision = self.decide()
            
            if decision == '1':
                self.plant_bushels()
            elif decision == '2':
                self.buy_land()
            elif decision == '3':
                self.sell_land()
            elif decision == '4':
                self.feed_people()
            elif decision == '5':
                self.end_year()

            if self.population <= 0:
                print("Your population has died out. You lose!")
                break

        if self.year > 10:
            print("Congratulations! You survived 10 years.")

    def plant_bushels(self):
        amount = int(self.get_input("How many bushels do you want to plant? "))
        if amount > self.bushels:
            print("You don't have enough bushels!")
            return
        self.bushels -= amount
        print(f"You planted {amount} bushels.")

    def buy_land(self):
        acres = int(self.get_input("How many acres do you want to buy? "))
        cost = acres * 20
        if cost > self.bushels:
            print("You don't have enough bushels!")
            return
        self.bushels -= cost
        self.land += acres
        print(f"You bought {acres} acres.")

    def sell_land(self):
        acres = int(self.get_input("How many acres do you want to sell? "))
        if acres > self.land:
            print("You don't have that much land!")
            return
        self.land -= acres
        self.bushels += acres * 20
        print(f"You sold {acres} acres.")

    def feed_people(self):
        amount = int(self.get_input("How many bushels do you want to feed the people? "))
        if amount > self.bushels:
            print("You don't have enough bushels!")
            return
        self.bushels -= amount
        fed_population = min(self.population, amount // 20)
        self.population -= (self.population - fed_population)
        print(f"You fed {fed_population} people.")

    def end_year(self):
        self.year += 1
        self.check_events()
        self.population += random.randint(-5, 5)  # Random population change
        print("Year ended.")

    def check_events(self):
        if random.random() < self.historical_events['plague'][0]:
            self.plague_years += 1
            self.population -= self.population // 10
            print("A plague has struck! 10% of the population has died.")
        if random.random() < self.historical_events['famine'][1]:
            self.population -= self.population // 20
            print("A famine has occurred! 5% of the population has died.")

if __name__ == "__main__":
    game = Hammurabi()
    game.play()