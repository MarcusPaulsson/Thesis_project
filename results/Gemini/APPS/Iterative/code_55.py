def calculate_intersection_area(x1, y1, x2, y2, x3, y3, x4, y4):
    ix1 = max(x1, x3)
    iy1 = max(y1, y3)
    ix2 = min(x2, x4)
    iy2 = min(y2, y4)
    
    if ix1 < ix2 and iy1 < iy2:
        return (ix2 - ix1) * (iy2 - iy1)
    else:
        return 0

def solve():
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    x5, y5, x6, y6 = map(int, input().split())

    white_area = (x2 - x1) * (y2 - y1)

    intersection1_area = calculate_intersection_area(x1, y1, x2, y2, x3, y3, x4, y4)
    intersection2_area = calculate_intersection_area(x1, y1, x2, y2, x5, y5, x6, y6)
    
    ix1 = max(x1, x3)
    iy1 = max(y1, y3)
    ix2 = min(x2, x4)
    iy2 = min(y2, y4)

    kx1, ky1, kx2, ky2 = 0, 0, 0, 0
    if ix1 < ix2 and iy1 < iy2:
        kx1 = max(ix1, x5)
        ky1 = max(iy1, y5)
        kx2 = min(ix2, x6)
        ky2 = min(iy2, y6)
    
    intersection12_area = 0
    if kx1 < kx2 and ky1 < ky2:
        intersection12_area = (kx2 - kx1) * (ky2 - ky1)

    covered_area = intersection1_area + intersection2_area - intersection12_area

    if white_area > covered_area:
        print("YES")
    else:
        print("NO")

solve()