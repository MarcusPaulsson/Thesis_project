def solve():
  x1, y1, x2, y2 = map(int, input().split())
  x3, y3, x4, y4 = map(int, input().split())
  x5, y5, x6, y6 = map(int, input().split())

  white_area = (x2 - x1) * (y2 - y1)

  # Calculate intersection with first black sheet
  x_overlap1 = max(0, min(x2, x4) - max(x1, x3))
  y_overlap1 = max(0, min(y2, y4) - max(y1, y3))
  intersection_area1 = x_overlap1 * y_overlap1

  # Calculate intersection with second black sheet
  x_overlap2 = max(0, min(x2, x6) - max(x1, x5))
  y_overlap2 = max(0, min(y2, y6) - max(y1, y5))
  intersection_area2 = x_overlap2 * y_overlap2
    
  # Calculate intersection between the two black sheets
  x_overlap_black = max(0, min(x4, x6) - max(x3, x5))
  y_overlap_black = max(0, min(y4, y6) - max(y3, y5))
  black_intersection_area = x_overlap_black * y_overlap_black
    
  # Calculate the intersection of all three rectangles
  x_overlap_all = max(0, min(x2, x4, x6) - max(x1, x3, x5))
  y_overlap_all = max(0, min(y2, y4, y6) - max(y1, y3, y5))
  all_intersection_area = x_overlap_all * y_overlap_all
    
  # Calculate intersection of white and both black sheets
  intersection_area12 = 0
  x_overlap_12 = max(0, min(x2, x4, x6) - max(x1, x3, x5))
  y_overlap_12 = max(0, min(y2, y4, y6) - max(y1, y3, y5))
  intersection_area12 = x_overlap_12 * y_overlap_12

  
  total_covered_area = intersection_area1 + intersection_area2 - all_intersection_area
  
  if white_area > total_covered_area:
    print("YES")
  else:
    print("NO")

solve()