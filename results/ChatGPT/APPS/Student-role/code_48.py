def min_trades(t, test_cases):
    results = []
    for x, y, k in test_cases:
        # Calculate total sticks needed
        total_sticks_needed = k + k * y
        
        # Calculate how many sticks we need to buy
        sticks_to_buy = total_sticks_needed - 1  # We start with 1 stick
        
        # Calculate trades for sticks
        trades_for_sticks = (sticks_to_buy + (x - 1)) // (x - 1)  # ceil(sticks_to_buy / (x - 1))
        
        # Calculate trades for coal
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
for res in results:
    print(res)