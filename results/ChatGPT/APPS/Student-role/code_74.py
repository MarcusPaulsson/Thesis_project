def maximize_army(T, test_cases):
    results = []
    
    for case in test_cases:
        n, k, minions = case
        # Sort minions based on their initial power and boost effect
        minions.sort(key=lambda x: (-x[0], -x[1]))
        
        actions = []
        current_minions = []
        current_power = 0
        
        for i in range(n):
            a_i, b_i = minions[i]
            # Summon the minion
            actions.append(i + 1)  # Summon minion i (1-based index)
            current_minions.append(a_i + sum(b for _, b in current_minions))
            current_power += current_minions[-1]
            
            # If we exceed the number of controllable minions, destroy the weakest one
            if len(current_minions) > k:
                # Find the index of the weakest minion
                weakest_index = current_minions.index(min(current_minions))
                # Destroy that minion
                actions.append(-(weakest_index + 1))  # Destroy minion (1-based index)
                current_power -= current_minions[weakest_index]
                current_minions.pop(weakest_index)
        
        # Result for this case
        results.append((len(actions), actions))
    
    return results

# Input reading
T = int(input())
test_cases = []

for _ in range(T):
    n, k = map(int, input().split())
    minions = [tuple(map(int, input().split())) for _ in range(n)]
    test_cases.append((n, k, minions))

# Get results
results = maximize_army(T, test_cases)

# Output results
for m, actions in results:
    print(m)
    print(" ".join(map(str, actions)))