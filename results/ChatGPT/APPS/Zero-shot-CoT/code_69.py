def min_cost_to_clear_mines(test_cases):
    results = []
    for a, b, mine_map in test_cases:
        n = len(mine_map)
        segments = 0
        i = 0
        
        # Count segments of continuous '1's
        while i < n:
            if mine_map[i] == '1':
                segments += 1
                while i < n and mine_map[i] == '1':
                    i += 1
            else:
                i += 1

        # Cost calculation
        if segments == 0:
            # No mines, no cost
            results.append(0)
        else:
            # Cost to activate all existing segments
            cost_to_activate_segments = segments * a
            
            # Cost to create a mine and then activate (if it is cheaper)
            # This is only applicable if there are gaps between mines
            cost_to_fill_gaps = (segments - 1) * b + a if segments > 1 else float('inf')
            
            # Minimum cost
            minimum_cost = min(cost_to_activate_segments, cost_to_fill_gaps)
            results.append(minimum_cost)

    return results

# Input reading
t = int(input())
test_cases = []
for _ in range(t):
    a, b = map(int, input().split())
    mine_map = input().strip()
    test_cases.append((a, b, mine_map))

# Get results
results = min_cost_to_clear_mines(test_cases)

# Output results
for result in results:
    print(result)