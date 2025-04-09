def solve():
    n = int(input())
    a = input()
    f = list(map(int, input().split()))

    a_list = list(map(int, list(a)))
    
    best_a = a
    
    for i in range(n):
        for j in range(i, n):
            temp_a_list = a_list[:]
            for k in range(i, j + 1):
                temp_a_list[k] = f[temp_a_list[k] - 1]
            
            temp_a = "".join(map(str, temp_a_list))
            
            if temp_a > best_a:
                best_a = temp_a
    
    print(best_a)

solve()