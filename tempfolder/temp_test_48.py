def min_trades(t, test_cases):
    results = []
    for i in range(t):
        x, y, k = test_cases[i]
        
        # Calculate the total sticks required
        total_sticks_needed = k + k * y
        
        # Calculate how many trades are needed to get the required sticks
        trades_for_sticks = (total_sticks_needed + (x - 2)) // (x - 1)
        
        # Total trades is the sum of trades for sticks and trades for coal
        total_trades = trades_for_sticks + k
        
        results.append(total_trades)
    
    return results

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()
t = int(data[0])
test_cases = [tuple(map(int, line.split())) for line in data[1:t + 1]]

# Get results and print them
results = min_trades(t, test_cases)
for result in results:
    print(result)