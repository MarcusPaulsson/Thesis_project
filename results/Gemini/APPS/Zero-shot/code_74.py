def solve():
    n, k = map(int, input().split())
    minions = []
    for _ in range(n):
        minions.append(list(map(int, input().split())))

    best_actions = []
    max_power = -1

    import itertools

    for perm in itertools.permutations(range(n)):
        for i in range(1 << n):
            actions = []
            army = []
            current_power = 0
            
            for idx in perm:
                actions.append(idx + 1)
                
                power_increase = 0
                for minion_idx in army:
                    power_increase += minions[idx][1]
                
                new_minion_power = minions[idx][0] + power_increase
                
                army.append(idx)
                current_power += new_minion_power
                
                if len(army) > k:
                    current_power -= new_minion_power
                    army.remove(idx)
                    current_power -= minions[idx][0]
                    
                    remove_idx = idx
                    actions.append(-(idx+1))
                    
                
            if current_power > max_power:
                max_power = current_power
                best_actions = actions
    
    print(len(best_actions))
    print(*best_actions)

t = int(input())
for _ in range(t):
    solve()