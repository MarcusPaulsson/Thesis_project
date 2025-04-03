def max_chess_score(test_cases):
    results = []
    
    for n, k, s in test_cases:
        # Calculate the initial score
        score = 0
        wins = []
        
        for i in range(n):
            if s[i] == 'W':
                if i == 0 or s[i - 1] == 'L':
                    score += 1
                else:
                    score += 2
                wins.append(i)
        
        # If we can change outcomes
        if k > 0:
            # Count the number of segments of losses
            segments = []
            last_lost = -1
            
            for i in range(n):
                if s[i] == 'L':
                    if last_lost == -1 or last_lost + 1 != i:
                        segments.append(1)
                    else:
                        segments[-1] += 1
                    last_lost = i
            
            # Count how many segments of losses we have
            num_segments = len(segments)
            
            # We can change at most k losses
            # Each segment can turn into wins if we have enough k
            total_wins = len(wins) + min(num_segments, k)
            additional_points = 0
            
            # Calculate the maximum score possible
            if total_wins > 0:
                additional_points = 1 + 2 * (total_wins - 1)
            
            score = max(score, additional_points)
        
        results.append(score)
    
    return results


# Reading input
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
test_cases = []

for i in range(t):
    n, k = map(int, data[i * 2 + 1].split())
    s = data[i * 2 + 2]
    test_cases.append((n, k, s))

# Get results
results = max_chess_score(test_cases)

# Print results
for result in results:
    print(result)