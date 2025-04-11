def solve():
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    x5, y5, x6, y6 = map(int, input().split())

    white_area = (x2 - x1) * (y2 - y1)
    
    # Intersection of white and black 1
    x_overlap1 = max(0, min(x2, x4) - max(x1, x3))
    y_overlap1 = max(0, min(y2, y4) - max(y1, y3))
    intersection_area1 = x_overlap1 * y_overlap1
    
    # Intersection of white and black 2
    x_overlap2 = max(0, min(x2, x6) - max(x1, x5))
    y_overlap2 = max(0, min(y2, y6) - max(y1, y5))
    intersection_area2 = x_overlap2 * y_overlap2
    
    # Intersection of white, black 1, and black 2
    x_overlap12 = max(0, min(x2, x4, x6) - max(x1, x3, x5))
    y_overlap12 = max(0, min(y2, y4, y6) - max(y1, y3, y5))
    intersection_area12 = x_overlap12 * y_overlap12
    
    total_covered_area = intersection_area1 + intersection_area2 - intersection_area12
    
    if white_area > total_covered_area:
        print("YES")
    else:
        print("NO")

solve()