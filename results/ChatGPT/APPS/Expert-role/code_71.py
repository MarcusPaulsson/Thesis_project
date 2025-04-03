def min_coins_to_zero(test_cases):
    results = []
    for case in test_cases:
        n, a = case
        coins = 0
        balance = 0
        
        for i in range(n):
            balance += a[i]
            if balance < 0:
                coins += -balance
                balance = 0
        
        results.append(coins)
    
    return results

# Input reading
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
test_cases = []

index = 1
for _ in range(t):
    n = int(data[index])
    a = list(map(int, data[index + 1].split()))
    test_cases.append((n, a))
    index += 2

# Get results
results = min_coins_to_zero(test_cases)

# Output results
for result in results:
    print(result)