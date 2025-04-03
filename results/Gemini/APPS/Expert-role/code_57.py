def solve():
    n = int(input())
    a = list(map(int, input().split()))

    def can_reduce(arr):
        if len(arr) == 1:
            return True
        
        for i in range(len(arr) - 1):
            if arr[i] < arr[i+1]:
                # Try removing arr[i]
                new_arr1 = arr[:i] + arr[i+1:]
                if can_reduce(new_arr1):
                    return True
                
                # Try removing arr[i+1]
                new_arr2 = arr[:i+1] + arr[i+2:]
                if can_reduce(new_arr2):
                    return True
        
        return False

    if can_reduce(a):
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    solve()