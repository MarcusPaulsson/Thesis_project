def transform_steps(n, m):
    if m % n != 0:
        return -1
    
    quotient = m // n
    count2 = 0
    count3 = 0
    
    while quotient % 2 == 0:
        quotient //= 2
        count2 += 1
        
    while quotient % 3 == 0:
        quotient //= 3
        count3 += 1
    
    if quotient != 1:
        return -1
    
    return count2 + count3

# Input reading
n, m = map(int, input().split())
print(transform_steps(n, m))