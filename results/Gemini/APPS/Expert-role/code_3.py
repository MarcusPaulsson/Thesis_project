def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    total_sum = sum(a)
    
    max_diff = 0
    
    sorted_a = sorted(a, reverse=True)
    
    max_diff = sum(sorted_a[:k+1])
    
    print(max_diff)

t = int(input())
for _ in range(t):
    solve()