def solve():
    n = int(input())
    a = input()
    f = list(map(int, input().split()))
    
    max_num = a
    
    for i in range(n):
        for j in range(i, n):
            temp_a = list(a)
            for k in range(i, j + 1):
                digit = int(a[k])
                temp_a[k] = str(f[digit - 1])
            
            new_num = "".join(temp_a)
            if new_num > max_num:
                max_num = new_num
                
    print(max_num)

solve()