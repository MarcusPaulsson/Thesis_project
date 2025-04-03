def longest_increasing_sequence(n, a):
    left, right = 0, n - 1
    last = float('-inf')
    moves = []
    
    while left <= right:
        if a[left] > last and (a[right] <= last or a[left] < a[right]):
            moves.append('L')
            last = a[left]
            left += 1
        elif a[right] > last:
            moves.append('R')
            last = a[right]
            right -= 1
        else:
            break
    
    print(len(moves))
    print(''.join(moves))

# Input reading
n = int(input())
a = list(map(int, input().split()))
longest_increasing_sequence(n, a)