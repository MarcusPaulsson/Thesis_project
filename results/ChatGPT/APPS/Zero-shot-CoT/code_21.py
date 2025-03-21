def find_min_k(n, S):
    S_set = set(S)
    
    # Check all possible values of k from 1 to 1023 (as k should be positive)
    for k in range(1, 1024):
        transformed_set = {s ^ k for s in S}
        if transformed_set == S_set:
            return k
    return -1

t = int(input())
for _ in range(t):
    n = int(input())
    S = list(map(int, input().split()))
    print(find_min_k(n, S))