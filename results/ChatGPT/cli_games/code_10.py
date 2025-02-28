import random

class HammurabiGame:
    def __init__(self):
        self.year = 1
        self.population = 100
        self.bushels = 2800
        self.land = 100
        self.plague = 0
        self.harvest_yield = 3
        self.famine_chance = 0.15
        self.plague_chance = 0.1
        self.misery = 0

    def play_game(self):
        while self.year <= 10:
            print(f"\nYear {self.year}")
            self.display_status()
            self.take_turn()
            self.check_game_over()
            self.year += 1

    def display_status(self):
        print(f"Population: {self.population}")
        print(f"Bushels of grain: {self.bushels}")
        print(f"Acres of land: {self.land}")
        print(f"Grain per person: {self.bushels // self.population if self.population else 0}")
        print(f"Misery Level: {self.misery}")

    def take_turn(self):
        self.check_events()
        self.ask_user()

    def check_events(self):
        if random.random() < self.plague_chance:
            self.plague = 1
            self.population -= self.population // 2
            print(f"A plague has struck! Half of your population has died.")
            self.misery += 1
        else:
            self.plague = 0

        if random.random() < self.famine_chance and self.bushels < self.population:
            print("There is a famine!")
            self.population -= (self.population - self.bushels // 20)
            self.misery += 1

    def ask_user(self):
        while True:
            try:
                acres_to_buy = int(input("How many acres do you wish to buy? "))
                if acres_to_buy < 0 or acres_to_buy * 20 > self.bushels:
                    print("Invalid number of acres.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")

        self.land += acres_to_buy
        self.bushels -= acres_to_buy * 20

        while True:
            try:
                bushels_to_feed = int(input("How many bushels do you wish to feed your people? "))
                if bushels_to_feed < 0 or bushels_to_feed > self.bushels:
                    print("Invalid number of bushels.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")

        self.bushels -= bushels_to_feed
        self.harvest_yield = self.land * 3
        self.bushels += self.harvest_yield

        self.population += bushels_to_feed // 20

    def check_game_over(self):
        if self.population <= 0:
            print("Your population has died out. Game over!")
            exit()
        if self.year == 10:
            print("Game over! Here are your final stats:")
            self.display_status()
            exit()

if __name__ == "__main__":
    game = HammurabiGame()
    game.play_game()