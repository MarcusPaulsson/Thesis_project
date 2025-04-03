def min_trades(t, test_cases):
    results = []
    for x, y, k in test_cases:
        # Calculate the total number of sticks needed
        total_sticks_needed = k + k * y  # k sticks for k coals + k coals for k torches
        # Calculate the number of trades to get the required sticks
        trades_for_sticks = (total_sticks_needed + x - 1) // (x - 1)  # ceiling of total_sticks_needed / (x - 1)
        # Total trades = trades for sticks + trades for coal (which is k)
        total_trades = trades_for_sticks + k
        results.append(total_trades)
    return results

# Read input
t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]

# Calculate and print results
results = min_trades(t, test_cases)
for res in results:
    print(res)