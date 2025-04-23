def solve():
    n = int(input())
    a = input()
    f = list(map(int, input().split()))

    a_list = list(map(int, list(a)))

    best_a_list = a_list[:]

    start_index = -1
    end_index = -1

    for i in range(n):
        if f[a_list[i] - 1] > a_list[i]:
            start_index = i
            break

    if start_index != -1:
        end_index = start_index
        for i in range(start_index, n):
            if f[a_list[i] - 1] >= a_list[i]:
                end_index = i
            else:
                break

        for i in range(start_index, end_index + 1):
            best_a_list[i] = f[a_list[i] - 1]

    print("".join(map(str, best_a_list)))

solve()