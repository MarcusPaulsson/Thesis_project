d, k, a, b, t = map(int, input().split())

# The time if Vasiliy walks the entire distance
min_time = d * b

# Calculate the maximum number of full k segments he can drive
full_segments = d // k
remaining_distance = d % k

# Calculate the time taken if using the car for full segments and walking the rest
car_time = full_segments * (k * a + t) + remaining_distance * a
if full_segments > 0:
    car_time -= t  # Remove the last repair time if the last segment is not needed

min_time = min(min_time, car_time)

# Check time for all possible numbers of segments driven by car
for i in range(1, full_segments + 1):
    # i segments driven by car, remaining distances walked
    distance_driven = i * k
    distance_walked = d - distance_driven
    
    if distance_walked >= 0:
        current_time = (i * (k * a + t) + distance_walked * b)
        current_time -= t  # Remove the last repair time if not needed
        min_time = min(min_time, current_time)

# Consider the case of driving the last segment partially if there's remaining distance
if remaining_distance > 0:
    current_time = (full_segments * (k * a + t) + remaining_distance * a)
    if full_segments > 0:
        current_time -= t  # Remove the last repair time if the last segment is not needed
    min_time = min(min_time, current_time)

print(min_time)