def solve():
    n, k = map(int, input().split())
    t = input()
    
    if n == 1:
        print(t * k)
        return
    
    overlap = 0
    for i in range(1, n):
        if t[:n-i] == t[i:]:
            overlap = n - i
            break
    
    result = t + t[overlap:] * (k - 1)
    print(result)

solve()