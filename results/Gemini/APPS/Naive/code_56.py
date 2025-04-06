def solve():
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    x5, y5, x6, y6 = map(int, input().split())

    white_area = (x2 - x1) * (y2 - y1)

    def intersection_area(x1, y1, x2, y2, x3, y3, x4, y4):
        x_overlap = max(0, min(x2, x4) - max(x1, x3))
        y_overlap = max(0, min(y2, y4) - max(y1, y3))
        return x_overlap * y_overlap

    black1_on_white = intersection_area(x1, y1, x2, y2, x3, y3, x4, y4)
    black2_on_white = intersection_area(x1, y1, x2, y2, x5, y5, x6, y6)

    # Area of intersection between black1 and black2
    black1_black2_intersect_x1 = max(x3, x5)
    black1_black2_intersect_y1 = max(y3, y5)
    black1_black2_intersect_x2 = min(x4, x6)
    black1_black2_intersect_y2 = min(y4, y6)
    
    black1_black2_intersection = intersection_area(x3, y3, x4, y4, x5, y5, x6, y6)
    black1_black2_on_white = intersection_area(x1, y1, x2, y2, black1_black2_intersect_x1, black1_black2_intersect_y1, black1_black2_intersect_x2, black1_black2_intersect_y2) if black1_black2_intersection > 0 else 0

    total_covered = black1_on_white + black2_on_white - black1_black2_on_white

    if white_area > total_covered:
        print("YES")
    else:
        print("NO")

solve()