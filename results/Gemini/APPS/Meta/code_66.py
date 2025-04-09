def solve():
    n, k = map(int, input().split())
    t = input()
    
    if k == 1:
        print(t)
        return
    
    max_overlap = 0
    for overlap in range(n - 1, 0, -1):
        if t[:overlap] == t[n - overlap:]:
            max_overlap = overlap
            break
    
    s = t
    for _ in range(k - 1):
        s += t[max_overlap:]
    
    print(s)

solve()