def solve():
    n = int(input())
    segments = []
    for _ in range(n):
        l, r = map(int, input().split())
        segments.append((l, r))
    
    max_len = 0
    for i in range(n):
        temp_segments = segments[:i] + segments[i+1:]
        
        intersection_start = -1
        intersection_end = -1
        
        if not temp_segments:
            continue
        
        intersection_start = temp_segments[0][0]
        intersection_end = temp_segments[0][1]
        
        for l, r in temp_segments[1:]:
            intersection_start = max(intersection_start, l)
            intersection_end = min(intersection_end, r)
        
        if intersection_start <= intersection_end:
            max_len = max(max_len, intersection_end - intersection_start)
        
    print(max_len)

solve()