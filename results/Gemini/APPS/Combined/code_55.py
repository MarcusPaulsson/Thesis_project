def calculate_intersection_area(x1, y1, x2, y2, x3, y3, x4, y4):
    """Calculates the area of intersection between two rectangles."""
    intersection_x1 = max(x1, x3)
    intersection_y1 = max(y1, y3)
    intersection_x2 = min(x2, x4)
    intersection_y2 = min(y2, y4)

    width = max(0, intersection_x2 - intersection_x1)
    height = max(0, intersection_y2 - intersection_y1)

    return width * height


def solve():
    """Solves the problem of determining if a white sheet is fully covered by two black sheets."""
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    x5, y5, x6, y6 = map(int, input().split())

    white_area = (x2 - x1) * (y2 - y1)

    intersection1_area = calculate_intersection_area(x1, y1, x2, y2, x3, y3, x4, y4)
    intersection2_area = calculate_intersection_area(x1, y1, x2, y2, x5, y5, x6, y6)
    intersection12_area = calculate_intersection_area(x3, y3, x4, y4, x5, y5, x6, y6)
    intersection_all_area = calculate_intersection_area(x1, y1, x2, y2, min(x3,x5), min(y3,y5),max(x4,x6),max(y4,y6))

    
    total_covered_area = intersection1_area + intersection2_area - calculate_intersection_area(
        max(x1, x3, x5), max(y1, y3, y5), min(x2, x4, x6), min(y2, y4, y6),x1,y1,x2,y2
    )
    

    if white_area > total_covered_area:
        print("YES")
    else:
        print("NO")


solve()