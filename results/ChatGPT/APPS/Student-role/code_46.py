def maximize_wins(test_cases):
    results = []
    for s in test_cases:
        count_R = s.count('R')
        count_S = s.count('S')
        count_P = s.count('P')
        
        # We choose the move that beats the most frequent move of the bot
        if count_R >= count_S and count_R >= count_P:
            results.append('P' * len(s))  # Paper beats Rock
        elif count_S >= count_R and count_S >= count_P:
            results.append('R' * len(s))  # Rock beats Scissors
        else:
            results.append('S' * len(s))  # Scissors beat Paper
    return results

# Input reading
t = int(input())
test_cases = [input().strip() for _ in range(t)]

# Getting the results
results = maximize_wins(test_cases)

# Output the results
for result in results:
    print(result)