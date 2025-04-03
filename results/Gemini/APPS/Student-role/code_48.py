def solve():
    x, y, k = map(int, input().split())
    
    # We need k torches, so we need k coal.
    # To get k coal, we need k * y sticks.
    # So we need a total of k + k * y sticks.
    
    # We start with 1 stick. We need k + k * y sticks.
    # So we need k + k * y - 1 more sticks.
    
    # Each trade of the first type gives us x - 1 sticks.
    # Let n be the number of trades of the first type.
    # Then n * (x - 1) >= k + k * y - 1
    # n >= (k + k * y - 1) / (x - 1)
    # n = ceil((k + k * y - 1) / (x - 1))
    
    n = (k + k * y - 1 + (x - 1) - 1) // (x - 1)
    
    # We need k trades of the second type to get k coal.
    
    print(n + k)

t = int(input())
for _ in range(t):
    solve()