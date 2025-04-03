def maximize_army_strength(test_cases):
    results = []
    for n, k, minions in test_cases:
        # Sort minions based on their initial power and the boost they provide
        minions.sort(key=lambda x: (x[0] + x[1] * (n - 1)), reverse=True)

        actions = []
        current_army = []

        for i in range(n):
            a_i, b_i = minions[i]
            actions.append(i + 1)  # summon minion i
            current_army.append((a_i, b_i))

            # If we exceed k, we need to destroy the weakest summoned minion
            if len(current_army) > k:
                # Find the minion with the lowest effective power after boost
                current_army.sort(key=lambda x: x[0] + x[1] * (len(current_army) - 1))
                weakest_minion = current_army.pop(0)
                actions.append(-(minions.index(weakest_minion) + 1))  # destroy that minion

        # Gather the results for this test case
        results.append(f"{len(actions)}")
        results.append(" ".join(map(str, actions)))
    
    return "\n".join(results)

# Read input
T = int(input())
test_cases = []
for _ in range(T):
    n, k = map(int, input().split())
    minions = [tuple(map(int, input().split())) for _ in range(n)]
    test_cases.append((n, k, minions))

# Get results
output = maximize_army_strength(test_cases)
print(output)