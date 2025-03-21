def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    moves = 0
    seen = set()
    
    while True:
        all_odd = True
        for x in a:
            if x % 2 == 0:
                all_odd = False
                break
        
        if all_odd:
            break
        
        even_nums = set()
        for x in a:
            if x % 2 == 0:
                even_nums.add(x)
        
        if not even_nums:
            break
            
        c = min(even_nums)
        if c in seen:
            
            even_nums.remove(c)
            if not even_nums:
                break
            c = min(even_nums)
        
        
        if c in seen:
            break
                
        seen.add(c)
        
        for i in range(n):
            if a[i] == c:
                a[i] //= 2
        moves += 1
    
    print(moves)

t = int(input())
for _ in range(t):
    solve()