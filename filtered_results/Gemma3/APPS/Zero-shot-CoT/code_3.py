def solve():
    n, q = map(int, input().split())
    painters = []
    for _ in range(q):
        l, r = map(int, input().split())
        painters.append((l, r))
    
    max_painted = 0
    
    for i in range(1 << q):
        if bin(i).count('1') != q - 2:
            continue
        
        selected_painters = []
        for j in range(q):
            if (i >> j) & 1:
                selected_painters.append(painters[j])
        
        painted_sections = set()
        for l, r in selected_painters:
            for x in range(l, r + 1):
                painted_sections.add(x)
        
        max_painted = max(max_painted, len(painted_sections))
    
    print(max_painted)

solve()