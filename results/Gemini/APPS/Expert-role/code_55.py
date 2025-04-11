def solve():
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    x5, y5, x6, y6 = map(int, input().split())

    white_area = (x2 - x1) * (y2 - y1)

    def intersection_area(x1, y1, x2, y2, x3, y3, x4, y4):
        x_overlap_start = max(x1, x3)
        x_overlap_end = min(x2, x4)
        y_overlap_start = max(y1, y3)
        y_overlap_end = min(y2, y4)

        if x_overlap_start < x_overlap_end and y_overlap_start < y_overlap_end:
            return (x_overlap_end - x_overlap_start) * (y_overlap_end - y_overlap_start)
        else:
            return 0

    intersection1 = intersection_area(x1, y1, x2, y2, x3, y3, x4, y4)
    intersection2 = intersection_area(x1, y1, x2, y2, x5, y5, x6, y6)
    intersection12 = intersection_area(x3, y3, x4, y4, x5, y5, x6, y6)
    intersection_white_12 = intersection_area(x1, y1, x2, y2, max(x3, x5), max(y3, y5), min(x4, x6), min(y4, y6))

    total_covered_area = intersection1 + intersection2 - intersection_area(x1, y1, x2, y2, x3, y3, x4, y4) - intersection_area(x1, y1, x2, y2, x5, y5, x6, y6) + intersection_area(max(x1, x3, x5), max(y1, y3, y5), min(x2, x4, x6), min(y2, y4, y6), max(x1, x3, x5), max(y1, y3, y5), min(x2, x4, x6), min(y2, y4, y6))
    
    intersection_1_2 = intersection_area(x3, y3, x4, y4, x5, y5, x6, y6)
    intersection_white_1 = intersection_area(x1, y1, x2, y2, x3, y3, x4, y4)
    intersection_white_2 = intersection_area(x1, y1, x2, y2, x5, y5, x6, y6)

    union_area = intersection_white_1 + intersection_white_2 - intersection_area(max(x1, x3, x5), max(y1, y3, y5), min(x2, x4, x6), min(y2, y4, y6), max(x1, x3, x5), max(y1, y3, y5), min(x2, x4, x6), min(y2, y4, y6))

    if white_area > union_area:
        print("YES")
    else:
        print("NO")

solve()