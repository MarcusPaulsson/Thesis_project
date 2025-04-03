def solve():
    n = int(input())
    a = input()
    f = list(map(int, input().split()))

    best_a = a
    
    for i in range(n):
        for j in range(i, n):
            temp_a = list(a)
            for k in range(i, j + 1):
                digit = int(a[k])
                temp_a[k] = str(f[digit - 1])
            
            temp_a_str = "".join(temp_a)
            
            if temp_a_str > best_a:
                best_a = temp_a_str
    
    print(best_a)

solve()