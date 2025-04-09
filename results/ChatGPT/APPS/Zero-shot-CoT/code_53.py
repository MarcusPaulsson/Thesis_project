n = int(input())
a = list(map(int, input().split()))

left = 0
right = n - 1
last_taken = -1
moves = []

while left <= right:
    if a[left] < a[right]:
        if a[left] > last_taken:
            moves.append('L')
            last_taken = a[left]
            left += 1
        else:
            if a[right] > last_taken:
                moves.append('R')
                last_taken = a[right]
                right -= 1
            else:
                break
    else:
        if a[right] > last_taken:
            moves.append('R')
            last_taken = a[right]
            right -= 1
        else:
            if a[left] > last_taken:
                moves.append('L')
                last_taken = a[left]
                left += 1
            else:
                break

print(len(moves))
print(''.join(moves))