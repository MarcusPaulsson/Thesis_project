def solve():
    n, k = map(int, input().split())
    t = input()
    
    max_overlap = 0
    for overlap in range(1, n):
        if t[:n-overlap] == t[overlap:]:
            max_overlap = n - overlap
            break
            
    if max_overlap == 0:
        print(t + t * (k - 1))
    else:
        print(t + t[max_overlap:] * (k - 1))

solve()