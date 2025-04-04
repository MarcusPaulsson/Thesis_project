def longest_increasing_sequence(n, a):
    left, right = 0, n - 1
    last_chosen = float('-inf')
    moves = []
    
    while left <= right:
        if a[left] > last_chosen and (a[right] <= last_chosen or a[left] < a[right]):
            moves.append('L')
            last_chosen = a[left]
            left += 1
        elif a[right] > last_chosen:
            moves.append('R')
            last_chosen = a[right]
            right -= 1
        else:
            break

    print(len(moves))
    print(''.join(moves))

# Input reading
n = int(input().strip())
a = list(map(int, input().strip().split()))

longest_increasing_sequence(n, a)