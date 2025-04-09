def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    nice_indices = []
    for i in range(n):
        temp_arr = a[:i] + a[i+1:]
        arr_sum = sum(temp_arr)
        
        for j in range(len(temp_arr)):
            if temp_arr[j] == arr_sum - temp_arr[j]:
                nice_indices.append(i + 1)
                break
    
    nice_indices = sorted(list(set(nice_indices)))
    print(len(nice_indices))
    print(*nice_indices)

solve()