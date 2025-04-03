def maximize_wins(t, test_cases):
    results = []
    for s in test_cases:
        count_R = s.count('R')
        count_P = s.count('P')
        count_S = s.count('S')
        
        # Choose the option that beats the most frequent move of the bot
        if count_R >= count_P and count_R >= count_S:
            results.append('P' * len(s))  # Paper beats Rock
        elif count_P >= count_R and count_P >= count_S:
            results.append('S' * len(s))  # Scissors beat Paper
        else:
            results.append('R' * len(s))  # Rock beats Scissors
    return results

# Input reading
t = int(input())
test_cases = [input().strip() for _ in range(t)]

# Get results
results = maximize_wins(t, test_cases)

# Output results
for result in results:
    print(result)