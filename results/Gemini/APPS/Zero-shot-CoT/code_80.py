def solve():
  n = int(input())
  s = input()
  
  colors = [0] * n
  
  def check(num_colors):
    assigned_colors = [0] * n
    tails = ['z' for _ in range(num_colors)]
    
    for i in range(n):
      found_color = False
      for color in range(num_colors):
        if s[i] >= tails[color]:
          assigned_colors[i] = color + 1
          tails[color] = s[i]
          found_color = True
          break
      if not found_color:
        return False
    
    
    colored_chars = []
    for i in range(n):
      colored_chars.append((s[i], assigned_colors[i]))

    return assigned_colors
  
  
  low = 1
  high = n
  ans = -1
  ans_colors = None
  
  while low <= high:
    mid = (low + high) // 2
    
    colors_result = check(mid)
    
    if colors_result:
      ans = mid
      ans_colors = colors_result
      high = mid - 1
    else:
      low = mid + 1
      
  print(ans)
  print(*ans_colors)
  
solve()