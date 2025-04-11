def longest_increasing_sequence(n, a):
    left, right = 0, n - 1
    last_taken = float('-inf')
    moves = []

    while left <= right:
        if a[left] > last_taken and (a[right] <= last_taken or a[left] < a[right]):
            last_taken = a[left]
            moves.append('L')
            left += 1
        elif a[right] > last_taken:
            last_taken = a[right]
            moves.append('R')
            right -= 1
        else:
            break

    return len(moves), ''.join(moves)

# Input reading
n = int(input())
a = list(map(int, input().split()))

# Function call and output
length, sequence = longest_increasing_sequence(n, a)
print(length)
print(sequence)