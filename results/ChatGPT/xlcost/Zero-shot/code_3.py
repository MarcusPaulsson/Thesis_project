def find_nth_number(n):
    result = 0
    p = 1
    
    while n > 0:
        n -= 1
        result += (n % 9) * p
        n //= 9
        p *= 10
    
    return result

# Driver code
N = 10  # Example input
print(find_nth_number(N))