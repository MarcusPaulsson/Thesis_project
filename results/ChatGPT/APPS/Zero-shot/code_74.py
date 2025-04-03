def maximize_army_power(test_cases):
    results = []
    
    for n, k, minions in test_cases:
        # Sort minions by their power increase (b_i) in descending order
        minions = sorted(enumerate(minions, start=1), key=lambda x: x[1][1], reverse=True)
        
        summoned = []
        total_power = 0
        
        for index, (a, b) in minions:
            if len(summoned) < k:
                # Summon the minion
                summoned.append((index, a + total_power))
                total_power += b
            else:
                # If we already have k minions, we need to decide which one to drop
                # Drop the one with the least effective total power
                min_power_index = min(range(len(summoned)), key=lambda i: summoned[i][1])
                if summoned[min_power_index][1] < a + total_power:
                    # Destroy the minion with the least effective power
                    results.append(f"-{summoned[min_power_index][0]}")
                    # Add the new minion
                    summoned[min_power_index] = (index, a + total_power)
                    total_power += b
                else:
                    results.append(f"-{index}")
        
        # Summon all selected minions
        for index, _ in summoned:
            results.append(f"{index}")
        
        results.insert(0, str(len(results)))
    
    return "\n".join(results)

# Input reading part
T = int(input())
test_cases = []
for _ in range(T):
    n, k = map(int, input().split())
    minions = [tuple(map(int, input().split())) for _ in range(n)]
    test_cases.append((n, k, minions))

# Execute the function and print results
output = maximize_army_power(test_cases)
print(output)