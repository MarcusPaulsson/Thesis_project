def solve():
    n = int(input())
    a = list(map(int, input().split()))

    nice_indices = []
    for i in range(n):
        temp_a = a[:i] + a[i+1:]
        total_sum = sum(temp_a)
        
        is_good = False
        for j in range(len(temp_a)):
            if temp_a[j] == total_sum - temp_a[j]:
                is_good = True
                break
        
        if is_good:
            nice_indices.append(i + 1)

    print(len(nice_indices))
    if nice_indices:
        print(*nice_indices)

solve()