def solve():
    n = int(input())
    s = input()
    
    ans = n
    
    for i in range(1, n // 2 + 1):
        prefix = s[:i]
        if s.startswith(prefix * 2):
            ans = min(ans, i + 1 + (n - 2 * i))
        elif s[:n - i] == prefix * 2 :
            ans = min(ans, n-i)
        elif s[i:] == prefix * 2:
            ans = min(ans, i+1)
        elif s.startswith(prefix) and len(prefix) <= n:
            if s[i:].startswith(prefix) and len(prefix) <= len(s[i:]):

                first_part = s[:i]
                second_part = s[i:]
                
                if second_part.startswith(first_part):
                  len_first_part = len(first_part)
                  len_second_part = len(second_part)
                  
                  
                  if len_second_part >= len_first_part:
                    
                    
                    ans = min(ans, len_first_part + 1 + len(second_part)-len_first_part)
                    
                
    
    print(ans)

solve()