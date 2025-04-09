def longest_increasing_sequence(n, a):
    left, right = 0, n - 1
    last_taken = -1
    moves = []

    while left <= right:
        if a[left] > last_taken and (a[right] <= last_taken or a[left] < a[right]):
            last_taken = a[left]
            moves.append('L')
            left += 1
        elif a[right] > last_taken:
            last_taken = a[right]
            moves.append('R')
            right -= 1
        else:
            break

    return len(moves), ''.join(moves)

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    length, sequence = longest_increasing_sequence(n, a)
    print(length)
    print(sequence)