def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    unique_elements = sorted(list(set(a)))
    
    if len(unique_elements) > k:
        print(-1)
        return
    
    while len(unique_elements) < k:
        unique_elements.append(1)
    
    beautiful_array = unique_elements * n
    
    print(len(beautiful_array))
    print(*beautiful_array)

t = int(input())
for _ in range(t):
    solve()