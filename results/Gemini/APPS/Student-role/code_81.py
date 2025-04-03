def solve():
  l, r = map(int, input().split())
  
  count = 0
  
  
  total_count = (r - l + 1) * (r - l) // 2
  
  
  num_zeros = max(0, l - 0)
  num_in_range = r - 0 + 1
  
  
  
  total_zeros = num_in_range * (num_in_range - 1) // 2
  
  total_zeros_below_l = max(0, l - 1) * (max(0, l - 1) - 1) // 2

  
  
  total_zeros_in_range = total_zeros - total_zeros_below_l
  
  
  
  
  count=0
  for a in range(l,r+1):
      for b in range(l,r+1):
          if a+b == a^b:
              count+=1
  
  final_count = 0
  for a in range(l, r + 1):
    for b in range(l, r + 1):
      if (a + b) == (a ^ b):
        final_count += 1
  
  
  print(final_count)
  
t = int(input())
for _ in range(t):
  solve()