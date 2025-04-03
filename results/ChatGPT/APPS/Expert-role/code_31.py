def calculate_time(test_cases):
    results = []
    for moves in test_cases:
        visited_segments = set()
        time = 0
        position = (0, 0)

        for move in moves:
            if move == 'N':
                new_position = (position[0], position[1] + 1)
            elif move == 'S':
                new_position = (position[0], position[1] - 1)
            elif move == 'E':
                new_position = (position[0] + 1, position[1])
            elif move == 'W':
                new_position = (position[0] - 1, position[1])

            segment = (position, new_position)
            if segment in visited_segments or (new_position, position) in visited_segments:
                time += 1  # Previously visited segment
            else:
                time += 5  # New segment
                visited_segments.add(segment)

            position = new_position

        results.append(time)
    
    return results

# Read input
t = int(input())
test_cases = [input().strip() for _ in range(t)]

# Calculate results
results = calculate_time(test_cases)

# Print output
for result in results:
    print(result)