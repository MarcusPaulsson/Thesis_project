def greatest_integer(t, cases):
    segments_needed = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]  # segments needed for digits 0-9
    results = []
    
    for n in cases:
        if n % 2 == 0:  # even case
            results.append('1' * (n // 2))
        else:  # odd case
            results.append('7' + '1' * (n // 2 - 1))
    
    return results

# Input reading
t = int(input().strip())
cases = [int(input().strip()) for _ in range(t)]

# Get results and print
results = greatest_integer(t, cases)
print("\n".join(results))