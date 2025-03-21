def max_score(t, test_cases):
    results = []
    
    for n, k, s in test_cases:
        score = 0
        consecutive_wins = 0
        changes = []

        # Calculate initial score and track segments of losses
        for i in range(n):
            if s[i] == 'W':
                consecutive_wins += 1
                score += 2 if i > 0 and s[i - 1] == 'W' else 1
            else:
                if consecutive_wins > 0:
                    changes.append(consecutive_wins)
                consecutive_wins = 0

        if consecutive_wins > 0:
            changes.append(consecutive_wins)

        # Count losses
        losses = s.count('L')
        
        # If we can change more losses than we have, we can convert all losses
        if k >= losses:
            # All wins can become consecutive
            score += (losses * 2) + 1  # All become W, first gets 1, others get 2
        else:
            # We can only change k losses
            changes.sort(reverse=True)
            
            # Total points from k changes
            score += k * 2  # Each change gives 2 points
            # Plus the initial score
            score += sum(changes[:k])  # Add scores from the remaining wins
            
            # If we can only change some of the losses
            if k > 0 and changes:
                # First game gets 1 point
                score += 1

        results.append(score)

    return results

# Input handling
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
test_cases = []

for i in range(1, 2*t, 2):
    n, k = map(int, data[i].split())
    s = data[i + 1]
    test_cases.append((n, k, s))

results = max_score(t, test_cases)

# Output results
sys.stdout.write('\n'.join(map(str, results)) + '\n')