def solve():
    cnt1 = int(input())
    cnt2 = int(input())
    cnt3 = int(input())
    cnt4 = int(input())

    if cnt1 == cnt4 and cnt1 >= 0 and cnt4 >= 0 and cnt3 >= 0 and cnt2 >= 0:
        if cnt1 == 0 and cnt3 > 0:
            print(0)
        else:
            print(1)
    else:
        print(0)

solve()