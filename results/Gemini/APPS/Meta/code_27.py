def solve():
    n = int(input())
    s = input()
    
    ans = n
    
    for i in range(1, n // 2 + 1):
        prefix = s[:i]
        if s[:2*i].startswith(prefix):
            
            
            
            if s.startswith(prefix * (n // i)):
                
                if n % i == 0:
                    ans = min(ans, i + 1)
                else:
                     ans = min(ans, i + 1 + (n % i))
            else:
                
                k = 1
                while prefix * k in s:
                  k+=1
                  if k*i > len(s):
                    break
                k-=1
                
                
                if prefix * k == s[:i*k]:
                    rem = s[i*k:]
                    ans = min(ans, i + 1 + len(rem))
                   
        
    print(ans)

solve()