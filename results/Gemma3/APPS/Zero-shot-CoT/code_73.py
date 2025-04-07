def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    def can_complete(arr):
        if len(set(arr)) == 1:
            return True
        
        for i in range(len(arr) - 1):
            if arr[i] == arr[i+1]:
                new_arr = arr[:]
                new_arr[i] += 1
                new_arr[i+1] += 1
                if can_complete(new_arr):
                    return True
        return False
    
    if can_complete(a):
        print("YES")
    else:
        print("NO")

solve()