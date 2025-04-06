def solve():
  n = int(input())
  
  weeks = n // 7
  remaining = n % 7
  
  min_days_off = weeks * 2
  max_days_off = weeks * 2
  
  if remaining == 1:
    min_days_off += 0
    max_days_off += 1
  elif remaining == 2:
    min_days_off += 0
    max_days_off += 2
  elif remaining == 3:
    min_days_off += 0
    max_days_off += 2
  elif remaining == 4:
    min_days_off += 0
    max_days_off += 2
  elif remaining == 5:
    min_days_off += 0
    max_days_off += 2
  elif remaining == 6:
    min_days_off += 1
    max_days_off += 2
  
  print(min_days_off, max_days_off)

solve()