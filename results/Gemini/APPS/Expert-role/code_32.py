def solve():
  n = int(input())
  
  curr_pos = 0  # 0 is North Pole, 20000 is South Pole
  
  for _ in range(n):
    t, direction = input().split()
    t = int(t)
    
    if curr_pos == 0:
      if direction != "South":
        print("NO")
        return
      else:
        curr_pos += t
    elif curr_pos == 20000:
      if direction != "North":
        print("NO")
        return
      else:
        curr_pos -= t
    else:
      if direction == "South":
        curr_pos += t
      elif direction == "North":
        curr_pos -= t
      
    if curr_pos < 0 or curr_pos > 20000:
      print("NO")
      return
      
  if curr_pos == 0:
    print("YES")
  else:
    print("NO")

solve()