def gift_distribution(n, friends):
    unknown = [i for i in range(1, n+1) if friends[i-1] == 0]
    known = [i for i in range(1, n+1) if friends[i-1] != 0]
    for i in range(len(unknown)):
        friends[unknown[i]-1] = known[i]
    return friends

n = int(input())
friends = list(map(int, input().split()))
print(*gift_distribution(n, friends))