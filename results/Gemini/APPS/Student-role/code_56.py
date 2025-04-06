def solve():
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    x5, y5, x6, y6 = map(int, input().split())

    white_area = (x2 - x1) * (y2 - y1)
    
    # Calculate intersection between white and black 1
    x_overlap_1 = max(0, min(x2, x4) - max(x1, x3))
    y_overlap_1 = max(0, min(y2, y4) - max(y1, y3))
    intersection_area_1 = x_overlap_1 * y_overlap_1
    
    # Calculate intersection between white and black 2
    x_overlap_2 = max(0, min(x2, x6) - max(x1, x5))
    y_overlap_2 = max(0, min(y2, y6) - max(y1, y5))
    intersection_area_2 = x_overlap_2 * y_overlap_2
    
    # Calculate intersection between all three rectangles
    x_overlap_12 = max(0, min(x2, x4, x6) - max(x1, x3, x5))
    y_overlap_12 = max(0, min(y2, y4, y6) - max(y1, y3, y5))
    intersection_area_12 = x_overlap_12 * y_overlap_12
    
    # Calculate intersection between black 1 and black 2
    x_overlap_blacks = max(0, min(x4, x6) - max(x3, x5))
    y_overlap_blacks = max(0, min(y4, y6) - max(y3, y5))
    intersection_area_blacks = x_overlap_blacks * y_overlap_blacks
    
    # Calculate the total area covered by black sheets within the white sheet
    total_covered_area = intersection_area_1 + intersection_area_2 - intersection_area_12
    
    if white_area > total_covered_area:
        print("YES")
    else:
        print("NO")

solve()