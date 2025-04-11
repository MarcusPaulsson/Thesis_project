n = int(input())
a = list(map(int, input().split()))

left, right = 0, n - 1
last_taken = -1
result = []
moves = []

while left <= right:
    if a[left] < a[right]:
        if a[left] > last_taken:
            last_taken = a[left]
            result.append(a[left])
            moves.append('L')
            left += 1
        elif a[right] > last_taken:
            last_taken = a[right]
            result.append(a[right])
            moves.append('R')
            right -= 1
        else:
            break
    else:
        if a[right] > last_taken:
            last_taken = a[right]
            result.append(a[right])
            moves.append('R')
            right -= 1
        elif a[left] > last_taken:
            last_taken = a[left]
            result.append(a[left])
            moves.append('L')
            left += 1
        else:
            break

print(len(result))
print(''.join(moves))