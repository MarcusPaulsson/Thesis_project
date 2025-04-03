def solve():
    a, b, p = map(int, input().split())
    s = input()
    n = len(s)
    
    cost = 0
    i = n - 2
    while i >= 0:
        j = i
        while j >= 0 and s[j] == s[i]:
            j -= 1
        
        if s[i] == 'A':
            cost += a
        else:
            cost += b
        
        i = j
        
    
    i = 0
    while i < n:
        
        temp_cost = 0
        
        j = n - 2
        
        
        temp_i = i
        temp_cost = 0
        
        while j >= temp_i:
            k = j
            while k >= temp_i and s[k] == s[j]:
                k -= 1
            
            if s[j] == 'A':
                temp_cost += a
            else:
                temp_cost += b
            
            j = k
        
        
        if temp_cost <= p:
            print(i + 1)
            return
        
        i += 1

t = int(input())
for _ in range(t):
    solve()