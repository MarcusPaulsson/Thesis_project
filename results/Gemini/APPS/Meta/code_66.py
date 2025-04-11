def solve():
    n, k = map(int, input().split())
    t = input()
    
    if k == 1:
        print(t)
        return
    
    max_overlap = 0
    for overlap in range(1, n):
        if t[:n-overlap] == t[overlap:]:
            max_overlap = n - overlap
            break
    
    result = t
    for _ in range(k - 1):
        result += t[max_overlap:]
    
    print(result)

solve()