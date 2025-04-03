def greatest_integer(t, cases):
    # Segments required for each digit
    segments = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    
    results = []
    for n in cases:
        if n % 2 == 0:
            # If n is even, we can use all segments to form the digit '1'
            results.append('1' * (n // 2))
        else:
            # If n is odd, we can use one '7' and the rest as '1's
            results.append('7' + '1' * ((n - 3) // 2))
    
    return results

# Read input
t = int(input())
cases = [int(input()) for _ in range(t)]

# Get results and print
results = greatest_integer(t, cases)
for result in results:
    print(result)