def solve():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    
    def kadane(arr):
        max_so_far = 0
        current_max = 0
        for i in range(len(arr)):
            current_max += arr[i]
            if current_max < 0:
                current_max = 0
            max_so_far = max(max_so_far, current_max)
        return max_so_far

    max_beauty = kadane(a)
    
    for i in range(n):
        for j in range(i, n):
            temp_a = a[:]
            for k in range(i, j + 1):
                temp_a[k] *= x
            max_beauty = max(max_beauty, kadane(temp_a))
            
    print(max_beauty)

solve()