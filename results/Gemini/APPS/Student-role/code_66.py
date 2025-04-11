def solve():
    n, k = map(int, input().split())
    t = input()
    
    overlap = 0
    for i in range(1, n):
        if t[:n-i] == t[i:]:
            overlap = n - i
            break
    
    if overlap == 0:
        print(t + t[n:] * (k - 1))
    else:
        print(t + t[overlap:] * (k - 1))

solve()