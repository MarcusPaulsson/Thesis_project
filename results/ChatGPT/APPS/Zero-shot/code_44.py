def min_time_to_post_office(d, k, a, b, t):
    time = float('inf')

    # Case 1: Walk the entire distance
    time = min(time, d * b)

    # Case 2: Use the car as much as possible
    full_cycles = d // k
    remaining_distance = d % k

    # Calculate time if using the car for full cycles
    if full_cycles > 0:
        time_using_car = (full_cycles * k * a) + (full_cycles - 1) * t + (remaining_distance * a if remaining_distance > 0 else 0)
        time = min(time, time_using_car)

    # Add walking time for remaining distance after using the car
    time_using_car = (full_cycles * k * a) + (full_cycles * t) + (remaining_distance * b)
    time = min(time, time_using_car)

    # Add time for using car and then walking
    if full_cycles > 0:
        time_using_car_and_walk = (full_cycles * k * a) + (full_cycles - 1) * t + (remaining_distance * b)
        time = min(time, time_using_car_and_walk)

    return time

# Input
d, k, a, b, t = map(int, input().split())
# Output
print(min_time_to_post_office(d, k, a, b, t))