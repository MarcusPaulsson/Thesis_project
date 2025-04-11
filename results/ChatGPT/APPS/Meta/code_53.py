def longest_increasing_sequence(n, a):
    left, right = 0, n - 1
    last_taken = -1
    result_length = 0
    result_moves = []

    while left <= right:
        if a[left] < a[right]:
            if a[left] > last_taken:
                last_taken = a[left]
                result_moves.append('L')
                result_length += 1
                left += 1
            else:
                break
        else:
            if a[right] > last_taken:
                last_taken = a[right]
                result_moves.append('R')
                result_length += 1
                right -= 1
            else:
                break

    print(result_length)
    print(''.join(result_moves))

# Example usage:
# n = int(input())
# a = list(map(int, input().split()))
# longest_increasing_sequence(n, a)