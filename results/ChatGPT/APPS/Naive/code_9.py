def find_grandpa_sofa(d, n, m, sofas, cnt_l, cnt_r, cnt_t, cnt_b):
    sofas_positions = []
    
    for idx in range(d):
        x1, y1, x2, y2 = sofas[idx]
        sofas_positions.append((min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)))
        
    for idx in range(d):
        count_l = count_r = count_t = count_b = 0
        x1, y1, x2, y2 = sofas_positions[idx]

        for jdx in range(d):
            if idx == jdx:
                continue
            sx1, sy1, sx2, sy2 = sofas_positions[jdx]
            
            if sx2 < x1:  # Sofa jdx is to the left of sofa idx
                count_l += 1
            elif sx1 > x2:  # Sofa jdx is to the right of sofa idx
                count_r += 1
            elif sy2 < y1:  # Sofa jdx is above sofa idx
                count_t += 1
            elif sy1 > y2:  # Sofa jdx is below sofa idx
                count_b += 1
        
        if (count_l == cnt_l and count_r == cnt_r and 
                count_t == cnt_t and count_b == cnt_b):
            return idx + 1  # 1-based index

    return -1

# Input reading
d = int(input().strip())
n, m = map(int, input().strip().split())
sofas = [tuple(map(int, input().strip().split())) for _ in range(d)]
cnt_l, cnt_r, cnt_t, cnt_b = map(int, input().strip().split())

# Output the result
print(find_grandpa_sofa(d, n, m, sofas, cnt_l, cnt_r, cnt_t, cnt_b))