import random

class Hammurabi:
    def __init__(self):
        self.year = 1
        self.bushels = 100
        self.population = 100
        self.land = 100
        self.plague = False
        self.famine = False
        self.harvest = 0
        self.deaths = 0

    def print_status(self):
        print(f"Year: {self.year}")
        print(f"Bushels: {self.bushels}")
        print(f"Population: {self.population}")
        print(f"Land: {self.land}")

    def get_user_input(self):
        while True:
            try:
                land_to_buy = int(input("How many acres of land do you want to buy? "))
                if land_to_buy < 0 or land_to_buy * 20 > self.bushels:
                    print("Invalid amount. You can't buy that much land.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")
        
        while True:
            try:
                bushels_to_feed = int(input("How many bushels do you want to feed your people? "))
                if bushels_to_feed < 0 or bushels_to_feed > self.bushels:
                    print("Invalid amount. You can't feed more than you have.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")
        
        while True:
            try:
                acres_to_plant = int(input("How many acres do you want to plant? "))
                if acres_to_plant < 0 or acres_to_plant > self.land:
                    print("Invalid amount. You can't plant more than you own.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")
        
        return land_to_buy, bushels_to_feed, acres_to_plant

    def update_game_state(self, land_to_buy, bushels_to_feed, acres_to_plant):
        if land_to_buy > 0:
            self.bushels -= land_to_buy * 20
            self.land += land_to_buy

        if bushels_to_feed > 0:
            bushels_per_person = bushels_to_feed // self.population
            self.deaths = self.population - bushels_per_person * 5
            if self.deaths > 0:
                self.population -= self.deaths

        self.harvest = acres_to_plant * random.randint(1, 6)
        self.bushels += self.harvest
        self.year += 1

    def check_game_over(self):
        if self.population <= 0:
            print("Your population has died out. You lose!")
            return True
        if self.year > 10:
            print("You have ruled for 10 years. You win!")
            return True
        return False

    def play(self):
        while True:
            self.print_status()
            land_to_buy, bushels_to_feed, acres_to_plant = self.get_user_input()
            self.update_game_state(land_to_buy, bushels_to_feed, acres_to_plant)
            if self.check_game_over():
                break

if __name__ == "__main__":
    game = Hammurabi()
    game.play()