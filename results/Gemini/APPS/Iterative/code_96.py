def solve():
    n = int(input())
    q = list(map(int, input().split()))

    for first_element in range(1, n + 1):
        p = [first_element]
        
        for i in range(n - 1):
            next_element = p[-1] + q[i]
            p.append(next_element)
        
        if all(1 <= x <= n for x in p) and len(set(p)) == n:
            print(*p)
            return
                
    print(-1)

solve()