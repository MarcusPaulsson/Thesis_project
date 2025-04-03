def maximize_minions(t, test_cases):
    results = []
    for case in test_cases:
        n, k, minions = case
        # Sort minions by their initial power
        minions = sorted(minions, key=lambda x: (x[0], -x[1]), reverse=True)
        
        actions = []
        current_power = [0] * n
        summoned = []
        
        for i in range(n):
            a_i, b_i = minions[i]
            if len(summoned) < k:
                # Summon the minion
                actions.append(i + 1)  # Summon action
                summoned.append(i)
                # Increase the power of already summoned minions
                for j in range(len(summoned) - 1):
                    current_power[summoned[j]] += b_i
            else:
                # If already at max capacity, consider replacing one
                weakest_idx = min(summoned, key=lambda x: current_power[x] + minions[x][0])
                if current_power[weakest_idx] + minions[weakest_idx][0] < a_i:
                    # Destroy the weakest minion
                    actions.append(-(weakest_idx + 1))  # Destroy action
                    summoned.remove(weakest_idx)
                    # Summon the new minion
                    actions.append(i + 1)  # Summon action
                    summoned.append(i)
                    # Update the power of already summoned minions
                    for j in range(len(summoned) - 1):
                        current_power[summoned[j]] += b_i
        
        # Finalize the power levels for the summoned minions
        for s in summoned:
            current_power[s] += minions[s][0]
        
        results.append((len(actions), actions))
    
    return results

# Input reading
T = int(input())
test_cases = []
for _ in range(T):
    n, k = map(int, input().split())
    minions = [tuple(map(int, input().split())) for _ in range(n)]
    test_cases.append((n, k, minions))

# Process and output results
results = maximize_minions(T, test_cases)
for m, actions in results:
    print(m)
    print(" ".join(map(str, actions)))