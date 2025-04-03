def find_grandpa_sofa(d, n, m, sofas, cnt_l, cnt_r, cnt_t, cnt_b):
    for i, (x1, y1, x2, y2) in enumerate(sofas, start=1):
        left = sum(x1 == x and y1 > y2 for x, y1, x2, y in sofas)
        right = sum(x1 == x and y1 < y2 for x, y1, x2, y in sofas)
        top = sum(y1 == y and x1 > x2 for x1, y, x2, y2 in sofas)
        bottom = sum(y1 == y and x1 < x2 for x1, y, x2, y2 in sofas)
        if left == cnt_l and right == cnt_r and top == cnt_t and bottom == cnt_b:
            return i
    return -1

# Read input
d = int(input())
n, m = map(int, input().split())
sofas = [tuple(map(int, input().split())) for _ in range(d)]
cnt_l, cnt_r, cnt_t, cnt_b = map(int, input().split())

# Find Grandpa Maks's sofa
print(find_grandpa_sofa(d, n, m, sofas, cnt_l, cnt_r, cnt_t, cnt_b))