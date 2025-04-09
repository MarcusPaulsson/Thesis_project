def solve():
    n, m, d = map(int, input().split())
    c = list(map(int, input().split()))

    total_length = sum(c)
    
    if d > n + 1:
        print("YES")
        result = [0] * n
        last = n
        for i in range(m - 1, -1, -1):
          for j in range(c[i]):
            result[last - 1] = i + 1
            last -= 1
        print(*result)
        return

    min_space = (m + 1) * (d - 1)
    if total_length + min_space > n + d - 1:
        print("NO")
        return

    print("YES")
    result = [0] * n
    
    pos = 0
    platform_positions = []
    
    for i in range(m):
      platform_positions.append(pos)
      pos += d - 1
    
    remaining_space = n - total_length - sum([x for x in platform_positions])
    
    for i in range(m):
      add = min(remaining_space, d - 1)
      platform_positions[i] += add
      remaining_space -= add
    
    last = n
    for i in range(m - 1, -1, -1):
      
      start = last - c[i]
      
      while start < platform_positions[i]:
        start += 1
      
      for j in range(start, last):
        result[j] = i + 1
      
      last = start
        
    print(*result)

solve()