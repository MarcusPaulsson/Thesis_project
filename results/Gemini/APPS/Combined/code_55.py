def intersection_area(x1, y1, x2, y2, x3, y3, x4, y4):
    """Calculates the area of intersection between two rectangles."""
    x_overlap = max(0, min(x2, x4) - max(x1, x3))
    y_overlap = max(0, min(y2, y4) - max(y1, y3))
    return x_overlap * y_overlap


def solve():
    """Reads input, calculates covered area, and prints the result."""
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    x5, y5, x6, y6 = map(int, input().split())

    white_area = (x2 - x1) * (y2 - y1)

    intersection1 = intersection_area(x1, y1, x2, y2, x3, y3, x4, y4)
    intersection2 = intersection_area(x1, y1, x2, y2, x5, y5, x6, y6)

    # Calculate the intersection of the two black rectangles
    intersection_black_rectangles = intersection_area(x3, y3, x4, y4, x5, y5, x6, y6)

    # Calculate the total covered area by the two black rectangles within the white rectangle
    total_covered_area = intersection1 + intersection2 - intersection_area(x1, y1, x2, y2, max(x3, x5), max(y3, y5), min(x4, x6), min(y4, y6))
    
    #Alternative calculation of total covered area
    #total_covered_area = intersection1 + intersection2 - intersection_area(max(x1,x3), max(y1,y3), min(x2,x4), min(y2,y4), max(x1,x5), max(y1,y5), min(x2,x6), min(y2,y6))

    if white_area > intersection1 + intersection2 - intersection_area(x3, y3, x4, y4, x5, y5, x6, y6):
        intersection_white_black1 = intersection_area(x1, y1, x2, y2, x3, y3, x4, y4)
        intersection_white_black2 = intersection_area(x1, y1, x2, y2, x5, y5, x6, y6)
        
        total_covered_area = intersection_white_black1 + intersection_white_black2 - intersection_area(max(x3, x5), max(y3, y5), min(x4, x6), min(y4, y6), x1, y1, x2, y2)
        
        if white_area > total_covered_area:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")


solve()