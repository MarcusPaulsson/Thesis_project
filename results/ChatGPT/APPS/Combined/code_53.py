def longest_increasing_sequence(n, a):
    left, right = 0, n - 1
    last_taken = -1
    moves = []
    
    while left <= right:
        if a[left] > last_taken and (a[right] <= last_taken or a[left] < a[right]):
            moves.append('L')
            last_taken = a[left]
            left += 1
        elif a[right] > last_taken:
            moves.append('R')
            last_taken = a[right]
            right -= 1
        else:
            break
    
    return len(moves), ''.join(moves)

# Input reading
n = int(input().strip())
a = list(map(int, input().strip().split()))

# Get the result
k, s = longest_increasing_sequence(n, a)

# Output the result
print(k)
print(s)