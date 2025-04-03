def solve():
    n = int(input())
    q = list(map(int, input().split()))
    
    for first_element in range(1, n + 1):
        p = [first_element]
        valid = True
        
        for i in range(n - 1):
            next_element = p[-1] + q[i]
            if next_element < 1 or next_element > n:
                valid = False
                break
            p.append(next_element)
        
        if valid:
            if len(set(p)) == n:
                print(*p)
                return
    
    print(-1)

solve()