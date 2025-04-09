def max_days(a, b, c):
    # Define the food schedule for each day of the week
    food_schedule = ['fish', 'rabbit', 'chicken', 'fish', 'chicken', 'rabbit', 'fish']
    
    # Function to calculate the number of days we can last starting from a given day
    def calculate_days(start_day):
        fish = a
        rabbit = b
        chicken = c
        days = 0
        
        # Loop through the week starting from the given day
        for i in range(7):
            day = (start_day + i) % 7
            if food_schedule[day] == 'fish':
                if fish > 0:
                    fish -= 1
                else:
                    break
            elif food_schedule[day] == 'rabbit':
                if rabbit > 0:
                    rabbit -= 1
                else:
                    break
            elif food_schedule[day] == 'chicken':
                if chicken > 0:
                    chicken -= 1
                else:
                    break
            days += 1
            
        return days
    
    max_days_count = 0
    
    # Check starting from each day of the week
    for start in range(7):
        max_days_count = max(max_days_count, calculate_days(start))
    
    return max_days_count

# Input reading
a, b, c = map(int, input().split())
print(max_days(a, b, c))