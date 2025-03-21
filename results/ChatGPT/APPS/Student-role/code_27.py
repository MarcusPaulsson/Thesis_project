def min_moves_to_odd(t, test_cases):
    results = []
    for case in test_cases:
        n, a = case
        seen = set()
        moves = 0
        
        for number in a:
            while number % 2 == 0:
                if number not in seen:
                    seen.add(number)
                    moves += 1
                number //= 2
        
        results.append(moves)
    
    return results

# Input handling
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

# Get results and print
results = min_moves_to_odd(t, test_cases)
for result in results:
    print(result)