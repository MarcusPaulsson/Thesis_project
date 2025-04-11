def solve():
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    x5, y5, x6, y6 = map(int, input().split())

    white_area = (x2 - x1) * (y2 - y1)

    def intersection_area(x1, y1, x2, y2, x3, y3, x4, y4):
        x_overlap = max(0, min(x2, x4) - max(x1, x3))
        y_overlap = max(0, min(y2, y4) - max(y1, y3))
        return x_overlap * y_overlap

    intersection1 = intersection_area(x1, y1, x2, y2, x3, y3, x4, y4)
    intersection2 = intersection_area(x1, y1, x2, y2, x5, y5, x6, y6)

    # Calculate the intersection of the two black sheets with the white sheet
    x_overlap_black = max(0, min(x4, x6) - max(x3, x5))
    y_overlap_black = max(0, min(y4, y6) - max(y3, y5))
    intersection_black_sheets = x_overlap_black * y_overlap_black

    intersection_all = intersection_area(x1, y1, x2, y2, max(x3, x5), max(y3, y5), min(x4, x6), min(y4, y6))

    covered_area = intersection1 + intersection2 - intersection_area(max(x1, x3, x5), max(y1, y3, y5), min(x2, x4, x6), min(y2, y4, y6), max(x3, x5), max(y3, y5), min(x4, x6), min(y4, y6))
    
    if white_area > covered_area:
        print("YES")
    else:
        print("NO")

solve()