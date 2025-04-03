def max_painted_sections(n, q, painters):
    painters.sort(key=lambda x: x[0])
    max_painted = 0
    for i in range(q-2):
        for j in range(i+1, q-1):
            for k in range(j+1, q):
                painted = max(painters[i][1], painters[j][1], painters[k][1]) - min(painters[i][0], painters[j][0], painters[k][0]) + 1
                max_painted = max(max_painted, painted)
    return max_painted

n, q = map(int, input().split())
painters = [tuple(map(int, input().split())) for _ in range(q)]
print(max_painted_sections(n, q, painters))