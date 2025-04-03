def min_trades(t, test_cases):
    results = []
    for i in range(t):
        x, y, k = test_cases[i]
        
        # To craft k torches, we need k coals and k sticks
        # Total sticks needed = k (for torches) + k * y (for coal)
        total_sticks_needed = k + k * y
        
        # We start with 1 stick
        sticks_needed = total_sticks_needed - 1
        
        # Calculate the number of trades needed to get the required sticks
        # Each trade gives us (x - 1) additional sticks
        if sticks_needed > 0:
            trades_for_sticks = (sticks_needed + (x - 2)) // (x - 1)
        else:
            trades_for_sticks = 0
        
        # Each coal requires 1 trade
        trades_for_coal = k
        
        # Total trades
        total_trades = trades_for_sticks + trades_for_coal
        results.append(total_trades)
    
    return results

# Read input
t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]

# Get results
results = min_trades(t, test_cases)

# Print results
for result in results:
    print(result)