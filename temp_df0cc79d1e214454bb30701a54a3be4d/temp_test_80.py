def solve():
    l, r = map(int, input().split())
    count = 0
    
    n = r - l + 1
    count = n * (n - 1) // 2
    
    num_zeros = 0
    for i in range(l, r + 1):
      if i == 0:
        num_zeros += 1
      elif i & (i-1) == 0:
        num_zeros += 1
    
    count += num_zeros * (n - num_zeros) + num_zeros * (num_zeros - 1) // 2
    
    print(count)

t = int(input())
for _ in range(t):
    solve()