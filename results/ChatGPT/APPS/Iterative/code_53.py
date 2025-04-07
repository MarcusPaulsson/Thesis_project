def longest_increasing_sequence(n, a):
    left, right = 0, n - 1
    last_taken = float('-inf')
    sequence = []
    moves = []
    
    while left <= right:
        can_take_left = a[left] > last_taken
        can_take_right = a[right] > last_taken
        
        if can_take_left and (not can_take_right or a[left] < a[right]):
            last_taken = a[left]
            sequence.append(a[left])
            moves.append('L')
            left += 1
        elif can_take_right:
            last_taken = a[right]
            sequence.append(a[right])
            moves.append('R')
            right -= 1
        else:
            break
    
    print(len(sequence))
    print(''.join(moves))

# Input reading
n = int(input())
a = list(map(int, input().split()))

longest_increasing_sequence(n, a)