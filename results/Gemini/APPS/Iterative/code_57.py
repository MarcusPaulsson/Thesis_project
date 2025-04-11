def solve():
    n = int(input())
    f = list(map(int, input().split()))

    givers = [i + 1 for i in range(n)]
    receivers = [i + 1 for i in range(n)]

    given = set()
    for val in f:
        if val != 0:
            given.add(val)

    need_to_give = []
    for i in range(n):
        if f[i] == 0:
            need_to_give.append(i)

    available_receivers = []
    for i in range(1, n + 1):
        if i not in given:
            available_receivers.append(i)

    for i in range(len(need_to_give)):
        giver_index = need_to_give[i]
        receiver = available_receivers[i]

        if receiver == giver_index + 1:
            for j in range(len(available_receivers)):
                if available_receivers[j] != giver_index + 1:
                    available_receivers[i], available_receivers[j] = available_receivers[j], available_receivers[i]
                    receiver = available_receivers[i]
                    break

        f[giver_index] = receiver

    print(*f)

solve()