def solve():
  n = int(input())

  # Calculate the number of full weeks
  full_weeks = n // 7

  # Calculate the minimum and maximum days off from the full weeks
  min_days_off = full_weeks * 2
  max_days_off = full_weeks * 2

  # Calculate the remaining days
  remaining_days = n % 7

  # Adjust the minimum and maximum days off based on the remaining days
  if remaining_days == 6:
    min_days_off += 1
  elif remaining_days >= 1:
    pass #min_days_off += 0
  
  max_days_off += min(remaining_days, 2)

  print(min_days_off, max_days_off)

solve()