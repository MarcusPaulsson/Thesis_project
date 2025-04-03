def min_coins_to_zero(test_cases):
    results = []
    for a in test_cases:
        n = len(a)
        coins = 0
        balance = 0
        
        for i in range(n):
            balance += a[i]
            if balance < 0:
                coins -= balance  # We need to pay for this deficit
                balance = 0  # Reset balance as we can only make it zero now
        
        results.append(coins)
    
    return results

# Input reading
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    test_cases.append(a)

# Get results
results = min_coins_to_zero(test_cases)

# Output results
for result in results:
    print(result)