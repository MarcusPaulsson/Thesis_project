def solve():
  x1, y1, x2, y2 = map(int, input().split())
  x3, y3, x4, y4 = map(int, input().split())
  x5, y5, x6, y6 = map(int, input().split())

  white_area = (x2 - x1) * (y2 - y1)

  
  def intersection_area(x1, y1, x2, y2, x3, y3, x4, y4):
      x_overlap = max(0, min(x2, x4) - max(x1, x3))
      y_overlap = max(0, min(y2, y4) - max(y1, y3))
      return x_overlap * y_overlap
      
  intersection_area1 = intersection_area(x1, y1, x2, y2, x3, y3, x4, y4)
  intersection_area2 = intersection_area(x1, y1, x2, y2, x5, y5, x6, y6)
  
  x_overlap12 = max(0, min(x4, x6) - max(x3, x5))
  y_overlap12 = max(0, min(y4, y6) - max(y3, y5))
  
  intersection_area12 = intersection_area(x1, y1, x2, y2, max(x3, x5), max(y3, y5), min(x4, x6), min(y4, y6))
  intersection_area3 = intersection_area(x3, y3, x4, y4, x5, y5, x6, y6)
  
  total_covered_area = intersection_area1 + intersection_area2 - intersection_area12


  if white_area > total_covered_area:
      print("YES")
  else:
      print("NO")

solve()