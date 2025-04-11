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
        
        all_numbers_present = True
        for i in range(1, n + 1):
            if i not in p:
                all_numbers_present = False
                break
        
        if all_numbers_present:
            print(*p)
            return
    
    print(-1)

solve()