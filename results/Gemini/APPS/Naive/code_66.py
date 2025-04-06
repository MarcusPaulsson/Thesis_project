def solve():
    n, k = map(int, input().split())
    t = input()
    
    max_overlap = 0
    for i in range(1, n):
        if t[:n-i] == t[i:]:
            max_overlap = n - i
            break
            
    if max_overlap == 0:
        print(t + t * (k - 1))
    else:
        print(t + t[max_overlap:] * (k - 1))

solve()