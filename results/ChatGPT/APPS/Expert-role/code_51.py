from collections import Counter
import sys

def find_x_and_y(divisors):
    count = Counter(divisors)
    common_divisors = [d for d in count if count[d] > 1]
    
    # The largest number in the list should be x or y
    x = max(divisors)
    y = 1
    
    # Remove the largest number from the count
    count[x] -= 1
    if count[x] == 0:
        del count[x]
    
    # Now we need to find y
    for d in count:
        if count[d] > 0:
            y = d
            break
    
    return x, y

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    divisors = list(map(int, sys.stdin.readline().strip().split()))
    
    x, y = find_x_and_y(divisors)
    print(x, y)