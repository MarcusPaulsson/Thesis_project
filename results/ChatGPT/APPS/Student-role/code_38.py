t = int(input())
for _ in range(t):
    n, k1, k2 = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    # Find the maximum card of each player
    max_a = max(a)
    max_b = max(b)
    
    # The player with the higher maximum card wins
    if max_a > max_b:
        print("YES")
    else:
        print("NO")