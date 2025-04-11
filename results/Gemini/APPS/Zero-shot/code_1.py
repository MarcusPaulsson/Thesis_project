def solve():
  x = int(input())
  s = str(x)
  n = len(s)
  
  best_num = x
  best_sum = sum(int(digit) for digit in s)
  
  for i in range(n):
    if s[i] == '0':
      continue
    
    current_num_str = s[:i] + str(int(s[i]) - 1) + '9' * (n - i - 1)
    current_num = int(current_num_str)
    current_sum = sum(int(digit) for digit in current_num_str)
    
    if current_sum > best_sum:
      best_sum = current_sum
      best_num = current_num
    elif current_sum == best_sum and current_num > best_num:
      best_num = current_num
      
  print(best_num)

solve()