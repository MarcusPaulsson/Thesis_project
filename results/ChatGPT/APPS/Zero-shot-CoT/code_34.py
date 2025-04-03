def greatest_integer(t, cases):
    # The segments needed to display each digit from 0 to 9
    segments = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    
    results = []
    for n in cases:
        if n % 2 == 0:
            # If n is even, we can use n // 2 digits of '1'
            results.append('1' * (n // 2))
        else:
            # If n is odd, we can use one '7' and (n - 3) // 2 digits of '1'
            results.append('7' + '1' * ((n - 3) // 2))
    
    return results

# Read input
t = int(input())
cases = [int(input()) for _ in range(t)]

# Get results
results = greatest_integer(t, cases)

# Print results
for result in results:
    print(result)