def solve():
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    x5, y5, x6, y6 = map(int, input().split())

    white_area = (x2 - x1) * (y2 - y1)

    # Calculate intersection with first black sheet
    x_overlap1 = max(0, min(x2, x4) - max(x1, x3))
    y_overlap1 = max(0, min(y2, y4) - max(y1, y3))
    intersection_area1 = x_overlap1 * y_overlap1

    # Calculate intersection with second black sheet
    x_overlap2 = max(0, min(x2, x6) - max(x1, x5))
    y_overlap2 = max(0, min(y2, y6) - max(y1, y5))
    intersection_area2 = x_overlap2 * y_overlap2

    # Calculate intersection between the two black sheets and the white sheet
    x_intersect_black = max(0, min(x4, x6) - max(x3, x5))
    y_intersect_black = max(0, min(y4, y6) - max(y3, y5))
    black_intersection = x_intersect_black * y_intersect_black

    x_overlap_all = max(0, min(x2, x4, x6) - max(x1, x3, x5))
    y_overlap_all = max(0, min(y2, y4, y6) - max(y1, y3, y5))
    intersection_area_all = x_overlap_all * y_overlap_all

    covered_area = intersection_area1 + intersection_area2 - intersection_area_all

    if white_area > covered_area:
        print("YES")
    else:
        print("NO")

solve()