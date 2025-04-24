def solve():
    n = int(input())
    segments = []
    for _ in range(n):
        l, r = map(int, input().split())
        segments.append((l, r))

    max_len = 0
    for i in range(n):
        temp_segments = segments[:i] + segments[i+1:]
        
        intersection_start = temp_segments[0][0]
        intersection_end = temp_segments[0][1]
        
        for j in range(1, len(temp_segments)):
            intersection_start = max(intersection_start, temp_segments[j][0])
            intersection_end = min(intersection_end, temp_segments[j][1])
        
        length = max(0, intersection_end - intersection_start)
        max_len = max(max_len, length)

    print(max_len)

solve()