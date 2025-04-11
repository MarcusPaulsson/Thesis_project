from collections import Counter
import sys

def find_x_y(divisors):
    count = Counter(divisors)
    x, y = 1, 1
    
    for d in count:
        if count[d] == 2:
            x *= d
            y *= d
        elif count[d] == 1:
            if x < y:
                x *= d
            else:
                y *= d
                
    return x, y

n = int(input().strip())
divisors = list(map(int, input().strip().split()))

x, y = find_x_y(divisors)
print(x, y)