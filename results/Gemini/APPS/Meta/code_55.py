def solve():
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    x5, y5, x6, y6 = map(int, input().split())

    white_area = (x2 - x1) * (y2 - y1)
    
    intersection1 = max(0, min(x2, x4) - max(x1, x3)) * max(0, min(y2, y4) - max(y1, y3))
    intersection2 = max(0, min(x2, x6) - max(x1, x5)) * max(0, min(y2, y6) - max(y1, y5))
    
    x_overlap = max(0, min(x4, x6) - max(x3, x5))
    y_overlap = max(0, min(y4, y6) - max(y3, y5))
    intersection12_temp = x_overlap * y_overlap
    intersection12 = max(0, min(x2, x4, x6) - max(x1, x3, x5)) * max(0, min(y2, y4, y6) - max(y1, y3, y5)) if x_overlap > 0 and y_overlap > 0 else 0

    covered_area = intersection1 + intersection2 - intersection12
    
    if white_area > covered_area:
        print("YES")
    else:
        print("NO")

solve()