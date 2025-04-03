def minimum_coins(test_cases):
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

# Input handling
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

# Calculate results
results = minimum_coins(test_cases)

# Output
for result in results:
    print(result)