n = int(input())
a = list(map(int, input().split()))

left, right = 0, n - 1
last_taken = float('-inf')
sequence = []
moves = []

while left <= right:
    if a[left] > last_taken and (a[right] <= last_taken or a[left] < a[right]):
        sequence.append(a[left])
        moves.append('L')
        last_taken = a[left]
        left += 1
    elif a[right] > last_taken:
        sequence.append(a[right])
        moves.append('R')
        last_taken = a[right]
        right -= 1
    else:
        break

print(len(sequence))
print(''.join(moves))