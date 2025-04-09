def solve():
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    x5, y5, x6, y6 = map(int, input().split())

    white_area = (x2 - x1) * (y2 - y1)
    
    # Calculate intersection of white and black 1
    x_overlap_1 = max(0, min(x2, x4) - max(x1, x3))
    y_overlap_1 = max(0, min(y2, y4) - max(y1, y3))
    intersection_area_1 = x_overlap_1 * y_overlap_1
    
    # Calculate intersection of white and black 2
    x_overlap_2 = max(0, min(x2, x6) - max(x1, x5))
    y_overlap_2 = max(0, min(y2, y6) - max(y1, y5))
    intersection_area_2 = x_overlap_2 * y_overlap_2

    # Calculate intersection of white, black 1, and black 2
    x_overlap_12 = max(0, min(x2, x4, x6) - max(x1, x3, x5))
    y_overlap_12 = max(0, min(y2, y4, y6) - max(y1, y3, y5))
    intersection_area_12 = x_overlap_12 * y_overlap_12
    
    # Calculate intersection of black 1 and black 2
    x_black_overlap = max(0, min(x4, x6) - max(x3, x5))
    y_black_overlap = max(0, min(y4, y6) - max(y3, y5))
    black_overlap_area = x_black_overlap * y_black_overlap
    
    # Calculate intersection of white with (black 1 U black 2)
    union_area = intersection_area_1 + intersection_area_2 - intersection_area_12

    if white_area > union_area:
        print("YES")
    else:
        print("NO")

solve()