def min_moves_to_odd(t, test_cases):
    results = []
    
    for n, a in test_cases:
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

# Input reading
t = int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

# Processing and output
results = min_moves_to_odd(t, test_cases)
for result in results:
    print(result)