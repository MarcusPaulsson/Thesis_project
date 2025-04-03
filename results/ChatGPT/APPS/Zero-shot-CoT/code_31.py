def skier_time(test_cases):
    results = []
    
    for path in test_cases:
        visited_segments = set()
        x, y = 0, 0  # Start position
        total_time = 0
        
        for move in path:
            if move == 'N':
                new_pos = (x, y + 1)
            elif move == 'S':
                new_pos = (x, y - 1)
            elif move == 'E':
                new_pos = (x + 1, y)
            elif move == 'W':
                new_pos = (x - 1, y)

            # Create a segment as a frozenset of the two points (to ensure uniqueness)
            segment = frozenset([new_pos, (x, y)])
            
            if segment not in visited_segments:
                total_time += 5
                visited_segments.add(segment)
            else:
                total_time += 1
            
            # Move to the new position
            x, y = new_pos
        
        results.append(total_time)
    
    return results


# Read input
t = int(input())
test_cases = [input().strip() for _ in range(t)]

# Get results
results = skier_time(test_cases)

# Print output
for res in results:
    print(res)