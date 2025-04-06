def solve():
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    x5, y5, x6, y6 = map(int, input().split())

    white_area = (x2 - x1) * (y2 - y1)

    
    def intersection_area(x1a, y1a, x2a, y2a, x1b, y1b, x2b, y2b):
        x_overlap = max(0, min(x2a, x2b) - max(x1a, x1b))
        y_overlap = max(0, min(y2a, y2b) - max(y1a, y1b))
        return x_overlap * y_overlap

    
    intersection1 = intersection_area(x1, y1, x2, y2, x3, y3, x4, y4)
    intersection2 = intersection_area(x1, y1, x2, y2, x5, y5, x6, y6)

    
    x_overlap_black = max(0, min(x4, x6) - max(x3, x5))
    y_overlap_black = max(0, min(y4, y6) - max(y3, y5))
    overlap_black_area = x_overlap_black * y_overlap_black

    intersection12 = intersection_area(x1, y1, x2, y2, max(x3,x5), max(y3,y5), min(x4,x6), min(y4,y6))
    overlap12 = intersection_area(x3, y3, x4, y4, x5, y5, x6, y6)

    intersection_all_three = intersection_area(x1,y1,x2,y2, max(x3,x5),max(y3,y5), min(x4,x6), min(y4,y6))
    covered_area = intersection1 + intersection2 - intersection12

    if white_area > covered_area:
        print("YES")
    else:
        print("NO")

solve()