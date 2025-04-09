def solve():
  n = int(input())
  s = input()
  
  ans = n
  
  for i in range(1, n // 2 + 1):
    prefix = s[:i]
    if s[:2*i].startswith(prefix) and s.startswith(prefix * 2):
      ans = min(ans, i + 1 + (n - 2*i))
    elif s.startswith(prefix) and s[i:].startswith(prefix) and len(prefix) <= len(s) and s[:i] == s[i:2*i] if i <= (len(s)-i )else False :
      ans = min(ans, i + 1 + max(0, n - 2*i))
    
  
  print(ans)
  
solve()