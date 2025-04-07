def solve():
    n, k = map(int, input().split())
    s = input()
    
    if k > (1 << n) - 1:
        print(-1)
        return
    
    subsequences = []
    for i in range(1 << n):
        subsequence = ""
        for j in range(n):
            if (i >> j) & 1:
                subsequence += s[j]
        if subsequence:
            subsequences.append(subsequence)
    
    subsequences = sorted(list(set(subsequences)), key=len)
    
    if len(subsequences) < k:
        print(-1)
        return
    
    total_cost = 0
    for i in range(k):
        total_cost += n - len(subsequences[i])
    
    print(total_cost)

solve()