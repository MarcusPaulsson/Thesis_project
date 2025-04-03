def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    min_time = float('inf')
    
    for i in range(1 << n):
        courier_time = 0
        petya_time = 0
        
        courier_indices = []
        petya_indices = []
        
        for j in range(n):
            if (i >> j) & 1:
                courier_indices.append(j)
                courier_time = max(courier_time, a[j])
            else:
                petya_indices.append(j)
                petya_time += b[j]
        
        min_time = min(min_time, max(courier_time, petya_time))
        
    print(min_time)

t = int(input())
for _ in range(t):
    solve()