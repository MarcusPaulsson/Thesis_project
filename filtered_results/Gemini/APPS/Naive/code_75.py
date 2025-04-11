def solve():
  a, b, c = map(int, input().split())
  
  weekly_schedule = [0, 1, 2, 0, 2, 1, 0] 
  
  best_days = 0
  
  for start_day in range(7):
    days = 0
    fish = a
    rabbit = b
    chicken = c
    
    current_day = start_day
    
    while True:
      food_type = weekly_schedule[current_day % 7]
      
      if food_type == 0:
        if fish > 0:
          fish -= 1
          days += 1
        else:
          break
      elif food_type == 1:
        if rabbit > 0:
          rabbit -= 1
          days += 1
        else:
          break
      else:
        if chicken > 0:
          chicken -= 1
          days += 1
        else:
          break
      
      current_day += 1
      
    best_days = max(best_days, days)
    
  print(best_days)

solve()