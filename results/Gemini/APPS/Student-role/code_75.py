def solve():
    n, k = map(int, input().split())
    minions = []
    for _ in range(n):
        minions.append(list(map(int, input().split())))

    best_actions = []
    max_power = -1

    import itertools
    for r in range(k + 1):
        for summoned in itertools.permutations(range(n), r):
            
            current_power = 0
            current_minions = []
            actions = []

            
            powers = []
            for i in range(len(summoned)):
                powers.append(minions[summoned[i]][0])
                for j in range(i):
                  powers[i] += minions[summoned[j]][1]
                  
            
            current_power = sum(powers)
            
            if current_power > max_power:
                max_power = current_power
                best_actions = []
                for idx in summoned:
                    best_actions.append(idx + 1)
            
            
            for num_destroyed in range(r + 1):
                for destroyed in itertools.combinations(range(r), num_destroyed):
                  
                    current_power = 0
                    current_minions = []
                    actions = []
                    
                    powers = []
                    for i in range(len(summoned)):
                        powers.append(minions[summoned[i]][0])
                        for j in range(i):
                          powers[i] += minions[summoned[j]][1]
                    
                    
                    for i in range(len(summoned)):
                        if i not in destroyed:
                            current_power += powers[i]
                            
                    if current_power > max_power:
                        max_power = current_power
                        best_actions = []
                        
                        temp_summoned = [i+1 for i in summoned]
                        temp_destroyed = [-(summoned[i]+1)for i in destroyed]
                        
                        
                        
                        
                        
                        temp_actions = []
                        
                        summon_idx = 0
                        destroy_idx = 0
                        
                        
                        
                        
                        for i in range (r + num_destroyed):
                            if destroy_idx < len(temp_destroyed) and \
                                temp_destroyed[destroy_idx] < 0 and \
                                -temp_destroyed[destroy_idx] == temp_summoned[summon_idx]:
                                temp_actions.append(temp_summoned[summon_idx])
                                temp_actions.append(temp_destroyed[destroy_idx])
                                summon_idx += 1
                                destroy_idx += 1
                            else:
                                temp_actions.append(temp_summoned[summon_idx])
                                summon_idx += 1
                        
                        best_actions = temp_actions
                        
    print(len(best_actions))
    print(*best_actions)



t = int(input())
for _ in range(t):
    solve()