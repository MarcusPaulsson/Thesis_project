import random

def play_hammurabi():
    """Plays the game Hammurabi."""

    year = 1
    population = 100
    grain_stores = 2800
    acres_owned = 1000
    bushels_per_acre = 3
    deaths_from_starvation = 0

    print("Congratulations, you are the newly appointed ruler of ancient Sumeria!")
    print("Your reign begins in a time of plenty.  However, you face challenges:")
    print(" - People will starve if you do not provide enough grain.")
    print(" - Rats will eat your grain if you store too much.")
    print(" - The price of land will vary from year to year.")
    print(" - The amount of grain harvested per acre will also vary.")
    print("You must rule wisely, or you will be deposed!")

    while year <= 10:
        print("\nYear", year)
        print("Population is", population)
        print("Grain stores are", grain_stores, "bushels")
        print("You own", acres_owned, "acres of land")
        print("Harvest was", bushels_per_acre, "bushels per acre")
        print("Deaths from starvation last year:", deaths_from_starvation)

        # Land Price
        land_price = random.randint(17, 23)
        print("Land is selling for", land_price, "bushels per acre")

        # Buy/Sell Land
        while True:
            try:
                land_to_buy = int(input("How many acres do you wish to buy? "))
                if land_to_buy < 0:
                    print("You can't buy a negative number of acres.")
                    continue
                if land_to_buy * land_price > grain_stores:
                    print("You do not have enough grain to buy that much land.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")

        grain_stores -= land_to_buy * land_price
        acres_owned += land_to_buy

        while True:
            try:
                land_to_sell = int(input("How many acres do you wish to sell? "))
                if land_to_sell < 0:
                    print("You can't sell a negative number of acres.")
                    continue
                if land_to_sell > acres_owned:
                    print("You do not own that much land.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")

        grain_stores += land_to_sell * land_price
        acres_owned -= land_to_sell

        # Feed People
        while True:
            try:
                grain_to_feed = int(input("How many bushels do you wish to feed your people? "))
                if grain_to_feed < 0:
                    print("You can't feed them a negative amount of grain.")
                    continue
                if grain_to_feed > grain_stores:
                    print("You do not have enough grain to feed them that much.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")

        grain_stores -= grain_to_feed

        # Planting
        while True:
            try:
                acres_to_plant = int(input("How many acres do you wish to plant with grain? "))
                if acres_to_plant < 0:
                    print("You can't plant a negative number of acres.")
                    continue
                if acres_to_plant > acres_owned:
                    print("You do not own that much land.")
                    continue
                if acres_to_plant > population * 10:
                    print("You do not have enough people to plant that many acres.")
                    continue
                if acres_to_plant > grain_stores:
                    print("You do not have enough grain to plant that many acres.")
                    continue

                break
            except ValueError:
                print("Please enter a valid number.")

        grain_stores -= acres_to_plant

        # Harvest
        bushels_per_acre = random.randint(1, 6)
        harvested_grain = acres_to_plant * bushels_per_acre
        grain_stores += harvested_grain

        # Rats
        rat_infestation = random.randint(0, 100)
        if rat_infestation < 40:
            rat_loss = int(grain_stores * random.uniform(0.1, 0.3))
            grain_stores -= rat_loss
            print("Rats ate", rat_loss, "bushels of grain!")
        else:
            rat_loss = 0

        # Starvation
        people_fed = grain_to_feed // 20  # Each person needs 20 bushels
        deaths_from_starvation = population - people_fed
        if deaths_from_starvation < 0:
            deaths_from_starvation = 0

        population -= deaths_from_starvation

        # Immigration
        immigration = int(random.uniform(0.05, 0.15) * (100 - deaths_from_starvation))
        if immigration < 0:
            immigration = 0 # avoid negative populations
        population += immigration

        if population <= 0:
            print("\nYour entire population has died.  Your reign is over.")
            break

        # Check for Deposition
        if deaths_from_starvation > population * 0.45:
            print("\nToo many people starved! You are deposed by the angry mob!")
            break
        
        year += 1

    # End Game
    if year > 10:
        print("\nYour reign has ended after 10 years.")
        print("You ruled", acres_owned, "acres of land with a population of", population, "people.")


if __name__ == "__main__":
    play_hammurabi()