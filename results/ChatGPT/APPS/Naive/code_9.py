def find_grandpa_sofa(d, n, m, sofas, counts):
    cnt_l, cnt_r, cnt_t, cnt_b = counts
    sofas_positions = []

    for i in range(d):
        x1, y1, x2, y2 = sofas[i]
        if x1 > x2 or (x1 == x2 and y1 > y2):
            x1, y1, x2, y2 = x2, y2, x1, y1
        sofas_positions.append((x1, y1, x2, y2))

    def count_relations(s_index):
        x1, y1, x2, y2 = sofas_positions[s_index]
        left = right = top = bottom = 0

        for j in range(d):
            if j == s_index:
                continue
            sx1, sy1, sx2, sy2 = sofas_positions[j]
            if sx2 < x1:  # sofa j is to the left of sofa s_index
                left += 1
            elif sx1 > x2:  # sofa j is to the right of sofa s_index
                right += 1
            if sy2 < y1:  # sofa j is above sofa s_index
                top += 1
            elif sy1 > y2:  # sofa j is below sofa s_index
                bottom += 1

        return left, right, top, bottom

    for i in range(d):
        left, right, top, bottom = count_relations(i)
        if (left == cnt_l and right == cnt_r and top == cnt_t and bottom == cnt_b):
            return i + 1  # return 1-based index

    return -1

# Input reading
d = int(input().strip())
n, m = map(int, input().strip().split())
sofas = [tuple(map(int, input().strip().split())) for _ in range(d)]
counts = tuple(map(int, input().strip().split()))

# Output the result
print(find_grandpa_sofa(d, n, m, sofas, counts))