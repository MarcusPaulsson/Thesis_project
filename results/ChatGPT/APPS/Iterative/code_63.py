def min_instability(n, a):
    if n <= 1:
        return 0  # Edge case: if there's 1 or fewer elements, instability is 0
    
    a.sort()
    # Calculate the instability after removing the smallest or largest element
    option1 = a[-1] - a[1]  # Remove the smallest element
    option2 = a[-2] - a[0]  # Remove the largest element
    return min(option1, option2)

n = int(input().strip())
a = list(map(int, input().strip().split()))
print(min_instability(n, a))