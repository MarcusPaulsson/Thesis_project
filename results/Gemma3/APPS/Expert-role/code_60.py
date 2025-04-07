def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    for i in range(1 << n):
        subsequence = []
        for j in range(n):
            if (i >> j) & 1:
                subsequence.append(a[j])
        
        if len(subsequence) >= 3:
            if subsequence == subsequence[::-1]:
                print("YES")
                return
    
    print("NO")

t = int(input())
for _ in range(t):
    solve()