def min_cost_to_clear_mines(test_cases):
    results = []
    
    for a, b, mine_map in test_cases:
        n = len(mine_map)
        segments = []
        i = 0
        
        # Identify segments of mines
        while i < n:
            if mine_map[i] == '1':
                start = i
                while i < n and mine_map[i] == '1':
                    i += 1
                segments.append((start, i - 1))  # Store the start and end of the segment
            else:
                i += 1
        
        # If there are no segments, cost is 0
        if not segments:
            results.append(0)
            continue
        
        # Calculate minimum cost
        total_cost = 0
        last_segment_end = segments[0][1]
        
        # Cost for the first segment
        total_cost += a
        
        # Evaluate gaps between segments
        for j in range(1, len(segments)):
            gap = segments[j][0] - last_segment_end - 1  # Gap between segments
            if gap > 0:
                # Check if placing a mine is cheaper than activating
                total_cost += min(a, gap * b)  # Activate the next segment or fill the gap
            total_cost += a  # Cost to activate the current segment
            last_segment_end = segments[j][1]
        
        results.append(total_cost)
    
    return results

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    a, b = map(int, input().split())
    mine_map = input().strip()
    test_cases.append((a, b, mine_map))

# Get results and print
results = min_cost_to_clear_mines(test_cases)
for result in results:
    print(result)