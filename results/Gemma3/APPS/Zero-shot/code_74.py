def solve():
    n, k = map(int, input().split())
    s = input()
    
    if k > 2**n - 1:
        print(-1)
        return
    
    subsequences = []
    for i in range(1 << n):
        subsequence = ""
        for j in range(n):
            if (i >> j) & 1:
                subsequence += s[j]
        subsequences.append(subsequence)
    
    unique_subsequences = []
    for sub in subsequences:
        if sub not in unique_subsequences:
            unique_subsequences.append(sub)
    
    if len(unique_subsequences) < k:
        print(-1)
        return
    
    
    costs = []
    for sub in unique_subsequences:
        costs.append(n - len(sub))
    
    costs.sort()
    
    total_cost = sum(costs[:k])
    
    print(total_cost)

solve()