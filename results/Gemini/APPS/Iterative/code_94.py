def solve():
  a, b, x = map(int, input().split())

  def construct_string(start_with_one):
    res = ""
    zeros_left = a
    ones_left = b
    changes_left = x
    
    current_char = "1" if start_with_one else "0"
    
    while changes_left > 0:
      if current_char == "1":
        if zeros_left > 0:
          res += "0"
          zeros_left -= 1
          current_char = "0"
          changes_left -= 1
        else:
          res += "1"
          ones_left -= 1
          changes_left -= 1
      else:
        if ones_left > 0:
          res += "1"
          ones_left -= 1
          current_char = "1"
          changes_left -= 1
        else:
          res += "0"
          zeros_left -= 1
          changes_left -= 1
    
    if zeros_left > 0:
      res += "0" * zeros_left
    if ones_left > 0:
      res += "1" * ones_left
    
    return res
  
  if a > b:
    print(construct_string(False))
  else:
    print(construct_string(True))

solve()