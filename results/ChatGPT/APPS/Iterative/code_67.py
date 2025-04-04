def find_nice_indices(n, a):
    total_sum = sum(a)
    nice_indices = []

    for i in range(n):
        if total_sum - a[i] == a[i]:
            nice_indices.append(i + 1)  # Store indices in 1-based format
    
    print(len(nice_indices))
    if nice_indices:
        print(' '.join(map(str, nice_indices)))

if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    
    if n > 0 and len(a) == n:
        find_nice_indices(n, a)
    else:
        print("Invalid input: Ensure the number of elements matches the specified count.")