import math

def solve():
  a, b = map(int, input().split())
  total = a + b
  
  best_perimeter = float('inf')
  
  for height in range(1, int(math.sqrt(total)) + 2):
    if total % height == 0:
      width = total // height
      
      # Case 1: 'a' forms a rectangle
      for a_height in range(1, int(math.sqrt(a)) + 2):
        if a % a_height == 0:
          a_width = a // a_height
          
          if a_height <= height and a_width <= width:
            best_perimeter = min(best_perimeter, 2 * (height + width))
      
      # Case 2: 'b' forms a rectangle
      for b_height in range(1, int(math.sqrt(b)) + 2):
        if b % b_height == 0:
          b_width = b // b_height
          
          if b_height <= height and b_width <= width:
            best_perimeter = min(best_perimeter, 2 * (height + width))
  
  print(best_perimeter)

solve()