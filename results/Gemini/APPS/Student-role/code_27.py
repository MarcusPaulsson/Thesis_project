def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    moves = 0
    processed = set()
    
    while True:
        all_odd = True
        for x in a:
            if x % 2 == 0:
                all_odd = False
                break
        
        if all_odd:
            break
        
        
        max_even = -1
        for x in a:
            if x % 2 == 0:
                max_even = max(max_even, x)
        
        if max_even == -1:
            break
        
        if max_even not in processed:
            processed.add(max_even)
            moves += 1
            
            for i in range(n):
                if a[i] == max_even:
                    a[i] //= 2
        else:
            
            changed = False
            for c in sorted(list(set([x for x in a if x % 2 == 0])), reverse=True):
                if c not in processed:
                    processed.add(c)
                    moves += 1
                    for i in range(n):
                        if a[i] == c:
                            a[i] //= 2
                    changed = True
                    break
            if not changed:
                break
            
    print(moves)
    

t = int(input())
for _ in range(t):
    solve()