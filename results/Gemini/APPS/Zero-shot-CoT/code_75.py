def solve():
    n, k = map(int, input().split())
    minions = []
    for _ in range(n):
        minions.append(list(map(int, input().split())))

    best_actions = []
    max_power = -1

    import itertools
    for r in range(n + 1):
        for summoned_indices in itertools.permutations(range(n), r):
            if r > 0:
                for kept_indices_set in itertools.combinations(summoned_indices, min(k, r)):
                    
                    actions = []
                    power = 0
                    army = {}
                    
                    for i in summoned_indices:
                        actions.append(i + 1)
                        army[i] = minions[i][0] 
                        
                        for j in army:
                            if j != i:
                                army[j] += minions[i][1]
                    
                    current_army = list(army.keys())
                    
                    for minion_index in current_army:
                        if minion_index not in kept_indices_set:
                            actions.append(-(minion_index + 1))
                            del army[minion_index]
                    
                    current_power = sum(army.values())
                    
                    if current_power > max_power:
                        max_power = current_power
                        best_actions = actions

    print(len(best_actions))
    print(*best_actions)


t = int(input())
for _ in range(t):
    solve()