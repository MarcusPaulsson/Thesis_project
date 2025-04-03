def find_sequence(n, k):
    # Minimum sum of first k positive integers is k * (k + 1) // 2
    min_sum = k * (k + 1) // 2
    if n < min_sum:
        return -1

    # The maximum gcd we can use
    g = (n - min_sum) // k + 1  # this is the maximum gcd we can use

    # We need to create the sequence
    result = [i * g for i in range(1, k + 1)]
    
    # Adjust the last element to make the sum equal to n
    result[-1] += (n - sum(result))

    return result

# Input reading
n, k = map(int, input().split())
result = find_sequence(n, k)
if result == -1:
    print(-1)
else:
    print(" ".join(map(str, result)))