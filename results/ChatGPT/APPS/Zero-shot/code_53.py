n = int(input())
a = list(map(int, input().split()))

left, right = 0, n - 1
last = -1
sequence = []
moves = []

while left <= right:
    if a[left] <= a[right]:
        if a[left] > last:
            last = a[left]
            sequence.append(a[left])
            moves.append('L')
            left += 1
        elif a[right] > last:
            last = a[right]
            sequence.append(a[right])
            moves.append('R')
            right -= 1
        else:
            break
    else:
        if a[right] > last:
            last = a[right]
            sequence.append(a[right])
            moves.append('R')
            right -= 1
        elif a[left] > last:
            last = a[left]
            sequence.append(a[left])
            moves.append('L')
            left += 1
        else:
            break

print(len(sequence))
print(''.join(moves))