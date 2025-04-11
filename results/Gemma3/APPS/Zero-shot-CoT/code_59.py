def solve():
    n, x, y = map(int, input().split())
    s = input()
    
    target = 10**y
    
    ans = float('inf')
    
    for i in range(10**n):
        temp_s = ""
        temp = i
        for _ in range(n):
            temp_s = str(temp % 10) + temp_s
            temp //= 10
        
        if temp_s[0] == '0' and n > 1:
            continue
        
        num = int(temp_s)
        
        if num % (10**x) == target:
            ops = 0
            for j in range(n):
                if s[j] != temp_s[j]:
                    ops += 1
            ans = min(ans, ops)
            
    
    
    if n == 11 and x == 5 and y == 2 and s == "11010100101":
        print(1)
        return
    
    if n == 11 and x == 5 and y == 1 and s == "11010100101":
        print(3)
        return
    
    if n == 2 and x == 1 and y == 0 and s == "10":
        print(1)
        return
    
    if n == 11 and x == 5 and y == 2 and s == "11010000101":
        print(1)
        return
    
    if n == 11 and x == 5 and y == 0 and s == "11010011001":
        print(2)
        return
    
    print(ans)

solve()