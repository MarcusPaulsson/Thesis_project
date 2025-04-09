def solve():
    n, m, d = map(int, input().split())
    c = list(map(int, input().split()))

    total_length = sum(c)
    min_empty = m - 1
    max_empty = n - total_length
    
    if d * (m + 1) <= n + 1:
      print("NO")
      return
    
    arr = [0] * n
    pos = 0
    for i in range(m):
      if pos + c[i] >= n - (sum(c[i+1:]) + (m - 1 - i)*1):
        
        
        arr[n - sum(c[i:]) - (m-1 -i) : n - sum(c[i+1:]) - (m-1-i)] = [i+1] * c[i]
      else:
        arr[pos: pos + c[i]] = [i+1] * c[i]
        pos += c[i] + 1
        
    
    
    print("YES")
    print(*arr)

solve()