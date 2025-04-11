def solve():
    n = int(input())
    a = input()
    f = list(map(int, input().split()))
    
    a_list = list(map(int, list(a)))
    
    best_a = a
    
    for i in range(n):
        for j in range(i, n):
            temp_a = a_list[:]
            for k in range(i, j + 1):
                temp_a[k] = f[temp_a[k] - 1]
            
            temp_str = "".join(map(str, temp_a))
            
            if temp_str > best_a:
                best_a = temp_str
                
    print(best_a)

solve()