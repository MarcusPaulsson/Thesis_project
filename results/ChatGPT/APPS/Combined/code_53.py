def longest_increasing_sequence(n, a):
    left, right = 0, n - 1
    last_taken = float('-inf')
    result_length = 0
    sequence = []

    while left <= right:
        if a[left] < a[right]:
            chosen = None
            if a[left] > last_taken:
                chosen = 'L'
            if a[right] > last_taken and (chosen is None or a[right] > a[left]):
                chosen = 'R'

            if chosen == 'L':
                last_taken = a[left]
                sequence.append(chosen)
                result_length += 1
                left += 1
            elif chosen == 'R':
                last_taken = a[right]
                sequence.append(chosen)
                result_length += 1
                right -= 1
            else:
                break
        else:
            chosen = None
            if a[right] > last_taken:
                chosen = 'R'
            if a[left] > last_taken and (chosen is None or a[left] > a[right]):
                chosen = 'L'

            if chosen == 'R':
                last_taken = a[right]
                sequence.append(chosen)
                result_length += 1
                right -= 1
            elif chosen == 'L':
                last_taken = a[left]
                sequence.append(chosen)
                result_length += 1
                left += 1
            else:
                break

    print(result_length)
    print(''.join(sequence))

# Read input
n = int(input())
a = list(map(int, input().split()))
longest_increasing_sequence(n, a)