def solve():
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    x5, y5, x6, y6 = map(int, input().split())

    def is_inside(x, y, x1, y1, x2, y2):
        return x1 < x < x2 and y1 < y < y2

    def is_outside(x, y, x1, y1, x2, y2):
        return not (x1 < x < x2 and y1 < y < y2)

    for x in range(x1, x2):
        for y in range(y1, y2):
            if is_outside(x, y, x3, y3, x4, y4) and is_outside(x, y, x5, y5, x6, y6):
                print("YES")
                return

    print("NO")

solve()