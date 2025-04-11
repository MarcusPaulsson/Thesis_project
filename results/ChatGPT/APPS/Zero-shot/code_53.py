n = int(input())
a = list(map(int, input().split()))

left, right = 0, n - 1
last = -1
result = []
moves = []

while left <= right:
    if a[left] > last and (a[right] <= last or a[left] < a[right]):
        result.append(a[left])
        moves.append('L')
        last = a[left]
        left += 1
    elif a[right] > last:
        result.append(a[right])
        moves.append('R')
        last = a[right]
        right -= 1
    else:
        break

print(len(result))
print(''.join(moves))