from collections import Counter
import sys

def find_x_y(n, divisors):
    count = Counter(divisors)
    x, y = 1, 1
    
    for d, freq in count.items():
        if freq == 2:
            x *= d
            y *= d
        elif freq == 1:
            if x > y:
                x *= d
            else:
                y *= d
                
    return x, y

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    divisors = list(map(int, sys.stdin.readline().strip().split()))
    
    x, y = find_x_y(n, divisors)
    print(x, y)