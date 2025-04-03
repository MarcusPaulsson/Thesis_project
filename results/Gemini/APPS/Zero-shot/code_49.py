def solve():
  l, r = map(int, input().split())
  
  def count_classy(n):
    s = str(n)
    length = len(s)
    
    dp = {}
    
    def recurse(index, non_zero_count, is_tight):
      if index == length:
        return 1
      
      if (index, non_zero_count, is_tight) in dp:
        return dp[(index, non_zero_count, is_tight)]
      
      ans = 0
      
      upper_bound = int(s[index]) if is_tight else 9
      
      for digit in range(upper_bound + 1):
        new_non_zero_count = non_zero_count + (1 if digit != 0 else 0)
        new_is_tight = is_tight and (digit == int(s[index]))
        
        if new_non_zero_count <= 3:
          ans += recurse(index + 1, new_non_zero_count, new_is_tight)
      
      dp[(index, non_zero_count, is_tight)] = ans
      return ans
    
    return recurse(0, 0, True)

  print(count_classy(r) - count_classy(l - 1))


t = int(input())
for _ in range(t):
  solve()