def intersection_area(x1, y1, x2, y2, x3, y3, x4, y4):
    """Calculates the area of intersection between two rectangles.

    Args:
        x1: x-coordinate of the bottom-left corner of the first rectangle.
        y1: y-coordinate of the bottom-left corner of the first rectangle.
        x2: x-coordinate of the top-right corner of the first rectangle.
        y2: y-coordinate of the top-right corner of the first rectangle.
        x3: x-coordinate of the bottom-left corner of the second rectangle.
        y3: y-coordinate of the bottom-left corner of the second rectangle.
        x4: x-coordinate of the top-right corner of the second rectangle.
        y4: y-coordinate of the top-right corner of the second rectangle.

    Returns:
        The area of the intersection between the two rectangles.
    """
    x_overlap = max(0, min(x2, x4) - max(x1, x3))
    y_overlap = max(0, min(y2, y4) - max(y1, y3))
    return x_overlap * y_overlap


def solve():
    """Reads input, calculates the visible area of the white sheet, and prints the result."""

    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    x5, y5, x6, y6 = map(int, input().split())

    white_area = (x2 - x1) * (y2 - y1)

    intersection1 = intersection_area(x1, y1, x2, y2, x3, y3, x4, y4)
    intersection2 = intersection_area(x1, y1, x2, y2, x5, y5, x6, y6)
    intersection12 = intersection_area(x3, y3, x4, y4, x5, y5, x6, y6)
    
    # Calculate the intersection of the white sheet with the union of the two black sheets.
    # This is equivalent to the area of the white sheet covered by either black sheet 1 or black sheet 2 or both.
    covered_area = intersection1 + intersection2 - intersection_area(x1, y1, x2, y2, max(x3, x5), max(y3, y5), min(x4, x6), min(y4, y6))

    if white_area > covered_area:
        print("YES")
    else:
        print("NO")


solve()