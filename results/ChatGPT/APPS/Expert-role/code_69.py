def min_cost_to_clear_mines(test_cases):
    results = []
    for a, b, mine_map in test_cases:
        n = len(mine_map)
        total_cost = 0
        i = 0
        
        while i < n:
            if mine_map[i] == '1':
                # We found a segment of mines
                while i < n and mine_map[i] == '1':
                    i += 1
                total_cost += a  # Activate the segment
            else:
                # Check if we are at the end of a segment of '0's
                start = i
                while i < n and mine_map[i] == '0':
                    i += 1
                if i < n and mine_map[i] == '1':  # There's a mine segment after
                    total_cost += b  # Place a mine to connect the segments
        
        results.append(total_cost)
    
    return results

# Reading input
import sys
input = sys.stdin.read

data = input().splitlines()
t = int(data[0])
test_cases = []

for i in range(t):
    a, b = map(int, data[2 * i + 1].split())
    mine_map = data[2 * i + 2]
    test_cases.append((a, b, mine_map))

# Getting results
results = min_cost_to_clear_mines(test_cases)

# Output results
for result in results:
    print(result)