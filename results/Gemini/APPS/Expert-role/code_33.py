def solve():
  n = int(input())
  
  current_nums = list(range(1, n + 1))
  
  for _ in range(n - 1):
    a = current_nums[-1]
    b = current_nums[-2]
    
    print(a, b)
    
    new_num = (a + b + 1) // 2
    
    current_nums = current_nums[:-2]
    current_nums.append(new_num)
    
  print(current_nums[0])

t = int(input())
for _ in range(t):
  solve()