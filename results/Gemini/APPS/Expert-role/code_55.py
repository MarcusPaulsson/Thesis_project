def solve():
  x1, y1, x2, y2 = map(int, input().split())
  x3, y3, x4, y4 = map(int, input().split())
  x5, y5, x6, y6 = map(int, input().split())

  white_area = (x2 - x1) * (y2 - y1)

  # Calculate intersection with black sheet 1
  x_overlap1 = max(0, min(x2, x4) - max(x1, x3))
  y_overlap1 = max(0, min(y2, y4) - max(y1, y3))
  overlap_area1 = x_overlap1 * y_overlap1

  # Calculate intersection with black sheet 2
  x_overlap2 = max(0, min(x2, x6) - max(x1, x5))
  y_overlap2 = max(0, min(y2, y6) - max(y1, y5))
  overlap_area2 = x_overlap2 * y_overlap2

  # Calculate intersection between black sheets and white sheet
  x_overlap12 = max(0, min(x2, x4, x6) - max(x1, x3, x5))
  y_overlap12 = max(0, min(y2, y4, y6) - max(y1, y3, y5))
  overlap_area12 = x_overlap12 * y_overlap12

  # Calculate intersection between black sheets
  x_black_overlap = max(0, min(x4, x6) - max(x3, x5))
  y_black_overlap = max(0, min(y4, y6) - max(y3, y5))
  black_overlap_area = x_black_overlap * y_black_overlap

  # Calculate covered area
  total_covered_area = overlap_area1 + overlap_area2 - max(0, min(x4,x6)-max(x3,x5))*max(0,min(y4,y6)-max(y3,y5))
  
  x_intersect = max(0, min(x2,x4,x6) - max(x1,x3,x5))
  y_intersect = max(0, min(y2,y4,y6) - max(y1,y3,y5))
  intersection_area = x_intersect * y_intersect

  covered_area = overlap_area1 + overlap_area2 - intersection_area

  if white_area > covered_area:
    print("YES")
  else:
    print("NO")

solve()