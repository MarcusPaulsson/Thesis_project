def solve():
    n, k = map(int, input().split())
    s = input()
    
    if k > (1 << n) - 1:
        print(-1)
        return
    
    subsequences = set()
    for i in range(1 << n):
        subsequence = ""
        for j in range(n):
            if (i >> j) & 1:
                subsequence += s[j]
        if subsequence:
            subsequences.add(subsequence)
    
    subsequences = sorted(list(subsequences))
    
    if len(subsequences) < k:
        print(-1)
        return
    
    costs = []
    for sub in subsequences:
        costs.append(n - len(sub))
    
    costs.sort()
    
    total_cost = sum(costs[:k])
    
    print(total_cost)

solve()