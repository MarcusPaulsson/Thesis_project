def skier_time(test_cases):
    results = []
    
    for moves in test_cases:
        visited_segments = set()
        current_position = (0, 0)
        total_time = 0
        
        for move in moves:
            if move == 'N':
                new_position = (current_position[0], current_position[1] + 1)
            elif move == 'S':
                new_position = (current_position[0], current_position[1] - 1)
            elif move == 'E':
                new_position = (current_position[0] + 1, current_position[1])
            elif move == 'W':
                new_position = (current_position[0] - 1, current_position[1])
            
            segment = (current_position, new_position) if current_position < new_position else (new_position, current_position)
            
            if segment not in visited_segments:
                total_time += 5
                visited_segments.add(segment)
            else:
                total_time += 1
            
            current_position = new_position
            
        results.append(total_time)
    
    return results

# Input handling
t = int(input())
test_cases = [input().strip() for _ in range(t)]
results = skier_time(test_cases)

# Output results
for result in results:
    print(result)