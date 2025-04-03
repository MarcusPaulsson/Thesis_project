def min_coins_to_zero(test_cases):
    results = []
    for n, a in test_cases:
        coins = 0
        balance = 0
        
        for i in range(n):
            balance += a[i]
            if balance < 0:
                coins += -balance
                balance = 0
        
        results.append(coins)
    return results

t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

results = min_coins_to_zero(test_cases)
for result in results:
    print(result)