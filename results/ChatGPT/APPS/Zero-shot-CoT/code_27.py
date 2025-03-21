def min_moves_to_odd(test_cases):
    results = []
    
    for case in test_cases:
        n, a = case
        moves = 0
        seen = set()

        for number in a:
            while number % 2 == 0:
                if number not in seen:
                    seen.add(number)
                    moves += 1
                number //= 2
        
        results.append(moves)
    
    return results


# Input reading
t = int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

# Get results
results = min_moves_to_odd(test_cases)

# Output results
for result in results:
    print(result)