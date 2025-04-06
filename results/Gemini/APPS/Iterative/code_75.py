def solve():
  a, b, c = map(int, input().split())
  
  days = ['fish', 'rabbit', 'chicken', 'fish', 'rabbit', 'chicken', 'fish']
  
  max_days = 0
  for start_day in range(7):
    curr_a = a
    curr_b = b
    curr_c = c
    
    curr_days = 0
    day_index = start_day
    
    while True:
      food = days[day_index % 7]
      
      if food == 'fish':
        if curr_a > 0:
          curr_a -= 1
          curr_days += 1
        else:
          break
      elif food == 'rabbit':
        if curr_b > 0:
          curr_b -= 1
          curr_days += 1
        else:
          break
      else:
        if curr_c > 0:
          curr_c -= 1
          curr_days += 1
        else:
          break
      
      day_index += 1
    
    max_days = max(max_days, curr_days)
    
  print(max_days)
  
solve()