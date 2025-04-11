def solve():
    n = int(input())
    q = list(map(int, input().split()))

    for first_element in range(1, n + 1):
        p = [first_element]
        valid = True
        for i in range(n - 1):
            next_element = p[-1] + q[i]
            p.append(next_element)
        
        if len(set(p)) != n:
            continue
        
        all_elements_present = True
        for i in range(n):
            if not (1 <= p[i] <= n):
                all_elements_present = False
                break
        
        if all_elements_present:
            seen = [False] * (n + 1)
            for x in p:
                if seen[x]:
                    all_elements_present = False
                    break
                seen[x] = True

        if all_elements_present:
            print(*p)
            return
    
    print(-1)

solve()