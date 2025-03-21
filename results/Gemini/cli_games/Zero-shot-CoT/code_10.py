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
        self.grain_stores = 2800
        self.acres_owned = 1000
        self.bushels_per_acre = 3
        self.deaths_from_starvation = 0
        self.immigrants = 0

    def summarize_year(self):
        """
        Prints a summary of the year's events.
        """
        print(f"\nYear {self.year} Summary:")
        print(f"Population: {self.population}")
        print(f"Acres owned: {self.acres_owned}")
        print(f"Grain stores: {self.grain_stores}")
        print(f"Harvest: {self.bushels_per_acre} bushels per acre")
        print(f"Deaths from starvation: {self.deaths_from_starvation}")
        print(f"Immigrants: {self.immigrants}")

    def ask_how_much_to_buy(self):
        """
        Asks the player how much grain to buy.

        Returns:
            The number of bushels to buy, or None if input is invalid.
        """
        while True:
            try:
                bushels_to_buy = int(input("How many bushels of grain do you wish to buy? "))
                if bushels_to_buy < 0:
                    print("Please enter a non-negative number.")
                elif bushels_to_buy * self.current_price > self.grain_stores:
                    print("You do not have enough grain to pay for that.")
                else:
                    return bushels_to_buy
            except ValueError:
                print("Invalid input. Please enter a number.")

    def ask_how_much_to_sell(self):
        """
        Asks the player how much grain to sell.

        Returns:
            The number of bushels to sell, or None if input is invalid.
        """
        while True:
            try:
                bushels_to_sell = int(input("How many bushels of grain do you wish to sell? "))
                if bushels_to_sell < 0:
                    print("Please enter a non-negative number.")
                elif bushels_to_sell > self.grain_stores:
                    print("You do not have that much grain to sell.")
                else:
                    return bushels_to_sell
            except ValueError:
                print("Invalid input. Please enter a number.")

    def ask_how_much_to_feed(self):
        """
        Asks the player how much grain to feed the people.

        Returns:
            The amount of grain to feed, or None if input is invalid.
        """
        while True:
            try:
                grain_to_feed = int(input("How many bushels of grain do you wish to feed your people? "))
                if grain_to_feed < 0:
                    print("Please enter a non-negative number.")
                elif grain_to_feed > self.grain_stores:
                    print("You do not have that much grain.")
                else:
                    return grain_to_feed
            except ValueError:
                print("Invalid input. Please enter a number.")

    def ask_how_much_to_plant(self):
        """
        Asks the player how many acres to plant with grain.

        Returns:
            The number of acres to plant, or None if input is invalid.
        """
        while True:
            try:
                acres_to_plant = int(input("How many acres do you wish to plant with grain? "))
                if acres_to_plant < 0:
                    print("Please enter a non-negative number.")
                elif acres_to_plant > self.acres_owned:
                    print("You do not own that much land.")
                elif acres_to_plant > self.grain_stores:
                    print("You do not have enough grain to plant that much.")
                elif acres_to_plant > self.population * 10:
                    print("You do not have enough people to plant that much land.")
                else:
                    return acres_to_plant
            except ValueError:
                print("Invalid input. Please enter a number.")

    def play_year(self):
        """
        Plays one year of the game.
        """

        self.current_price = random.randint(17, 23)

        print(f"\nYear {self.year}")
        print(f"The current price of land is {self.current_price} bushels per acre.")

        # Buy/Sell Land (Not Implemented)

        # Buy/Sell Grain
        buy_sell_choice = input("Do you want to buy or sell grain? (buy/sell/no): ").lower()
        if buy_sell_choice == "buy":
            bushels_to_buy = self.ask_how_much_to_buy()
            if bushels_to_buy is not None:
                self.grain_stores -= bushels_to_buy * self.current_price
                self.acres_owned += bushels_to_buy
                print(f"You bought {bushels_to_buy} acres of land.")
        elif buy_sell_choice == "sell":
            bushels_to_sell = self.ask_how_much_to_sell()
            if bushels_to_sell is not None:
                self.grain_stores += bushels_to_sell * self.current_price
                self.acres_owned -= bushels_to_sell
                print(f"You sold {bushels_to_sell} acres of land.")

        # Feed the people
        grain_to_feed = self.ask_how_much_to_feed()
        if grain_to_feed is not None:
            self.grain_stores -= grain_to_feed

        # Plant the grain
        acres_to_plant = self.ask_how_much_to_plant()
        if acres_to_plant is not None:
            self.grain_stores -= acres_to_plant
            
        # Harvest
        self.bushels_per_acre = random.randint(1, 6)
        harvested_grain = acres_to_plant * self.bushels_per_acre
        self.grain_stores += harvested_grain

        # Rats
        rat_infestation = random.randint(0, 1)
        if rat_infestation == 1:
            rat_loss = int(self.grain_stores * random.uniform(0.1, 0.3))
            self.grain_stores -= rat_loss
            print(f"Rats ate {rat_loss} bushels of grain!")
        else:
            print("No rats this year!")

        # Starvation and Immigration
        food_needed = self.population * 20
        if grain_to_feed < food_needed:
            starved = (food_needed - grain_to_feed) // 20
            if starved < 0:
                starved = 0
            self.deaths_from_starvation = starved
            self.population -= self.deaths_from_starvation
            if self.population <= 0:
                print("Your entire population has died. Game over.")
                return False
            print(f"{self.deaths_from_starvation} people starved this year.")
        else:
            self.deaths_from_starvation = 0
            
        immigrants = int(0.1 * (self.population - self.deaths_from_starvation))  # 10% increase
        self.immigrants = immigrants
        self.population += immigrants

        # Plague (chance of plague killing half the population)
        plague = random.randint(0, 9)  # 1 in 10 chance
        if plague == 0:
            plague_deaths = self.population // 2
            self.population -= plague_deaths
            print(f"A terrible plague has struck! {plague_deaths} people died.")

        self.summarize_year()
        self.year += 1
        return True

    def play_game(self):
        """
        Plays the entire game.
        """
        print("Welcome to Hammurabi!")
        while self.year <= 10:
            if not self.play_year():
                break

        if self.year > 10:
            print("\nCongratulations! You have ruled for 10 years.")
            print("Let's see how well you did:")
            print(f"You ended with {self.population} people.")
            print(f"You ended with {self.acres_owned} acres of land.")
            # Add a more detailed evaluation based on factors like population growth, land ownership, etc.
            land_per_person = self.acres_owned / self.population
            print(f"You have {land_per_person:.2f} acres of land per person.")
            if land_per_person > 12:
                print("A magnificent performance! Well done, mighty ruler!")
            elif land_per_person > 8:
                print("A good performance. You could have done better.")
            else:
                print("Your performance was poor. The people will remember your reign with disdain.")


if __name__ == '__main__':
    game = Hammurabi()
    game.play_game()