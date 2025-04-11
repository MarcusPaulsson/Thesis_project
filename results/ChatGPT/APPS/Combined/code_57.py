def assign_gifts(n, friends):
    givers = {i for i in range(1, n + 1) if i not in friends}
    receivers = {f for f in friends if f != 0}
    
    result = friends[:]
    givers = list(givers)
    giver_index = 0

    for i in range(n):
        if result[i] == 0:
            while giver_index < len(givers):
                if givers[giver_index] not in receivers and givers[giver_index] != i + 1:
                    result[i] = givers[giver_index]
                    giver_index += 1
                    break
                giver_index += 1

    return result

# Example usage
n = int(input())
friends = list(map(int, input().split()))
result = assign_gifts(n, friends)
print(' '.join(map(str, result)))