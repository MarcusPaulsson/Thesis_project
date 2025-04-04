def longest_increasing_sequence(n, a):
    left, right = 0, n - 1
    last_taken = float('-inf')
    result = []
    directions = []
    
    while left <= right:
        if a[left] < last_taken and a[right] < last_taken:
            break
        
        if a[left] >= last_taken and (a[right] < last_taken or a[left] <= a[right]):
            last_taken = a[left]
            result.append(last_taken)
            directions.append('L')
            left += 1
        elif a[right] >= last_taken:
            last_taken = a[right]
            result.append(last_taken)
            directions.append('R')
            right -= 1
    
    print(len(result))
    print(''.join(directions))

# Input reading
n = int(input())
a = list(map(int, input().split()))

longest_increasing_sequence(n, a)