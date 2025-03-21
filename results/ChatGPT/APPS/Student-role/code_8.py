def max_chess_score(t, test_cases):
    results = []
    
    for n, k, s in test_cases:
        current_score = 0
        win_streaks = []
        
        # Calculate current score and identify segments of W's
        i = 0
        while i < n:
            if s[i] == 'W':
                streak = 0
                while i < n and s[i] == 'W':
                    streak += 1
                    i += 1
                win_streaks.append(streak)
                current_score += 1 + (streak - 1) * 2
            else:
                i += 1
        
        # Calculate potential score gains by changing L's to W's
        gain = []
        for i in range(len(win_streaks) + 1):
            if i > 0:
                gain.append(win_streaks[i-1])  # potential gain from turning the L before the first W into W

            if i < len(win_streaks):
                if i + 1 < len(win_streaks):
                    gain.append(win_streaks[i] + win_streaks[i + 1])  # potential gain from merging two W streaks
        
        # Sort gains in descending order to use the most impactful changes first
        gain.sort(reverse=True)
        
        # Calculate the maximum score after changing at most k outcomes
        max_score = current_score
        for i in range(min(k, len(gain))):
            max_score += gain[i]
        
        results.append(max_score)
    
    return results

# Input reading and function call
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
test_cases = []

for i in range(1, 2 * t, 2):
    n, k = map(int, data[i].split())
    s = data[i + 1]
    test_cases.append((n, k, s))

results = max_chess_score(t, test_cases)

# Print results
for result in results:
    print(result)