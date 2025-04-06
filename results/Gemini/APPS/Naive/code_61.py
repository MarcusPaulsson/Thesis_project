def solve():
    n = int(input())
    a = input()
    f = list(map(int, input().split()))

    a_list = list(map(int, list(a)))
    
    best_a = a_list[:]
    
    for i in range(n):
        for j in range(i, n):
            temp_a = a_list[:]
            for k in range(i, j + 1):
                temp_a[k] = f[a_list[k] - 1]

            if temp_a > best_a:
                best_a = temp_a[:]

    print("".join(map(str, best_a)))

solve()