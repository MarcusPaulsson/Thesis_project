def solve():
    n, k = map(int, input().split())
    minions = []
    for _ in range(n):
        minions.append(list(map(int, input().split())))

    best_actions = []
    max_power = -1

    def calculate_power(current_minions):
        total_power = 0
        for power in current_minions:
            total_power += power
        return total_power

    def find_best_actions(available_minions, current_army, actions_taken):
        nonlocal best_actions, max_power

        current_power = calculate_power(current_army.values())

        if current_power > max_power:
            max_power = current_power
            best_actions = actions_taken[:]

        if not available_minions:
            return

        for i in range(len(available_minions)):
            minion_index = available_minions[i]
            a, b = minions[minion_index]

            # Option 1: Summon the minion
            if len(current_army) < k:
                new_army = current_army.copy()
                
                # Calculate the power of the current minion
                minion_power = a
                
                # Increase the power of existing minions
                for index in new_army:
                    new_army[index] += b

                new_army[minion_index] = minion_power
                
                
                new_available_minions = available_minions[:i] + available_minions[i+1:]
                new_actions_taken = actions_taken + [minion_index + 1]
                
                find_best_actions(new_available_minions, new_army, new_actions_taken)

                # Option 2: Summon and then destroy the minion
                
                new_army_destroy = current_army.copy()
                
                # Calculate the power of the current minion
                minion_power_destroy = a
                
                # Increase the power of existing minions
                for index in new_army_destroy:
                    new_army_destroy[index] += b

                
                
                
                if len(new_army_destroy) < k:
                    new_army_destroy[minion_index] = minion_power_destroy
                    new_army_destroy.pop(minion_index)
                else:
                    
                    new_army_destroy[minion_index] = minion_power_destroy

                    new_available_minions_destroy = available_minions[:i] + available_minions[i+1:]
                    new_actions_taken_destroy = actions_taken + [minion_index + 1, -(minion_index + 1)]

                    new_army_destroy.pop(minion_index)
                
                
                    find_best_actions(new_available_minions_destroy, new_army_destroy, new_actions_taken_destroy)
                else:
                    new_army_destroy.pop(minion_index, None)
                    
                    new_available_minions_destroy = available_minions[:i] + available_minions[i+1:]
                    new_actions_taken_destroy = actions_taken + [minion_index + 1, -(minion_index + 1)]
                    
                    if minion_index in current_army:
                        find_best_actions(new_available_minions_destroy, current_army, new_actions_taken_destroy)
                    else:
                        find_best_actions(new_available_minions_destroy, current_army, new_actions_taken_destroy)

    find_best_actions(list(range(n)), {}, [])

    print(len(best_actions))
    print(*best_actions)


t = int(input())
for _ in range(t):
    solve()