def solve():
  a, b, c = map(int, input().split())
  
  week = [0, 1, 2, 0, 2, 1, 0]  # 0: fish, 1: rabbit, 2: chicken
  
  weekly_a = week.count(0)
  weekly_b = week.count(1)
  weekly_c = week.count(2)
  
  weeks = min(a // weekly_a if weekly_a > 0 else float('inf'),
              b // weekly_b if weekly_b > 0 else float('inf'),
              c // weekly_c if weekly_c > 0 else float('inf'))
  
  a -= weeks * weekly_a
  b -= weeks * weekly_b
  c -= weeks * weekly_c
  
  days = weeks * 7
  
  best_days = 0
  
  for start_day in range(7):
    temp_days = 0
    temp_a, temp_b, temp_c = a, b, c
    
    possible = True
    
    while possible:
      day_index = (start_day + temp_days) % 7
      food_type = week[day_index]
      
      if food_type == 0:
        if temp_a > 0:
          temp_a -= 1
        else:
          possible = False
      elif food_type == 1:
        if temp_b > 0:
          temp_b -= 1
        else:
          possible = False
      else:
        if temp_c > 0:
          temp_c -= 1
        else:
          possible = False
      
      if possible:
        temp_days += 1
    
    best_days = max(best_days, temp_days)
  
  print(days + best_days)

solve()