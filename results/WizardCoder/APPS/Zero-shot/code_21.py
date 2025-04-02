def find_k(S):
    k = 0
    while True:
        new_set = {x ^ k for x in S}
        if new_set == set(S):
            return k
        else:
            k += 1

t = int(input())
for i in range(1, t + 1):
    n = int(input())
    S = set(map(int, input().split()))
    result = find_k(S)
    if result == float('inf'):
        print(-1)
    else:
        print(result)