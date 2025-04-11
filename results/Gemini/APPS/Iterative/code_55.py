def solve():
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    x5, y5, x6, y6 = map(int, input().split())

    white_area = (x2 - x1) * (y2 - y1)

    def intersection_area(x1, y1, x2, y2, x3, y3, x4, y4):
        x_overlap = max(0, min(x2, x4) - max(x1, x3))
        y_overlap = max(0, min(y2, y4) - max(y1, y3))
        return x_overlap * y_overlap

    intersection_area_1 = intersection_area(x1, y1, x2, y2, x3, y3, x4, y4)
    intersection_area_2 = intersection_area(x1, y1, x2, y2, x5, y5, x6, y6)

    # Intersection of black sheets
    x_overlap_black = max(0, min(x4, x6) - max(x3, x5))
    y_overlap_black = max(0, min(y4, y6) - max(y3, y5))
    intersection_area_black = x_overlap_black * y_overlap_black

    # Intersection of all three
    x_overlap_all = max(0, min(x2, x4, x6) - max(x1, x3, x5))
    y_overlap_all = max(0, min(y2, y4, y6) - max(y1, y3, y5))
    intersection_area_all = x_overlap_all * y_overlap_all

    covered_area = intersection_area_1 + intersection_area_2 - intersection_area_all

    if white_area > covered_area:
        print("YES")
    else:
        print("NO")

solve()