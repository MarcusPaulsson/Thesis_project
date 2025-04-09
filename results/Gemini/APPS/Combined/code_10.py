def solve():
  n = int(input())
  
  weeks = n // 7
  remaining_days = n % 7
  
  min_days_off = weeks * 2
  max_days_off = weeks * 2
  
  if remaining_days == 6:
    min_days_off += 1
  
  max_days_off += min(remaining_days, 2)
  
  print(min_days_off, max_days_off)

solve()