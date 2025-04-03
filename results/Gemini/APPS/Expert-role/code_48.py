def solve():
    x, y, k = map(int, input().split())
    
    # Need k coal, so need k * y sticks
    sticks_needed_for_coal = k * y
    
    # Need k sticks for torches
    total_sticks_needed = sticks_needed_for_coal + k
    
    # We start with 1 stick.  How many stick trades do we need?
    trades_for_sticks = (total_sticks_needed - 1 + (x - 2)) // (x - 1)
    
    print(trades_for_sticks + k)

t = int(input())
for _ in range(t):
    solve()