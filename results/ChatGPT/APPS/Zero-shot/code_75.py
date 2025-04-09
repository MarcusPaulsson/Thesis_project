def max_days(a, b, c):
    # Days of the week food distribution
    week_pattern = [0, 1, 0, 2, 0, 1, 2]  # 0: fish, 1: rabbit, 2: chicken
    food_count = [a, b, c]
    
    def can_feed_for_days(start_day, days):
        food_needed = [0, 0, 0]  # fish, rabbit, chicken
        
        for i in range(days):
            food_needed[week_pattern[(start_day + i) % 7]] += 1
        
        return all(food_needed[i] <= food_count[i] for i in range(3))

    max_days_possible = 0
    
    for start_day in range(7):
        left, right = 0, 10**18  # an arbitrary large number
        while left < right:
            mid = (left + right + 1) // 2
            if can_feed_for_days(start_day, mid):
                left = mid
            else:
                right = mid - 1
        max_days_possible = max(max_days_possible, left)
    
    return max_days_possible

# Read input
a, b, c = map(int, input().split())
# Output the result
print(max_days(a, b, c))