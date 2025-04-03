def maximize_wins(t, test_cases):
    results = []
    for s in test_cases:
        count_R = s.count('R')
        count_P = s.count('P')
        count_S = s.count('S')
        
        # Choose the move that beats the most common move of the bot
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

# Getting the results
results = maximize_wins(t, test_cases)

# Printing the results
for res in results:
    print(res)