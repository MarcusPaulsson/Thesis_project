def solve():
    d = int(input())
    n, m = map(int, input().split())
    sofas = []
    for _ in range(d):
        sofas.append(list(map(int, input().split())))
    cnt_l, cnt_r, cnt_t, cnt_b = map(int, input().split())

    def check_conditions(sofa_index):
        l_count = 0
        r_count = 0
        t_count = 0
        b_count = 0

        for i in range(d):
            if i == sofa_index:
                continue

            sofa1 = sofas[sofa_index]
            sofa2 = sofas[i]

            # Check left
            left_found = False
            for x1, y1 in [(sofa1[0], sofa1[1]), (sofa1[2], sofa1[3])]:
                for x2, y2 in [(sofa2[0], sofa2[1]), (sofa2[2], sofa2[3])]:
                    if y1 < y2:
                        left_found = True
                        break
                if left_found:
                    break
            if left_found:
                l_count += 1

            # Check right
            right_found = False
            for x1, y1 in [(sofa1[0], sofa1[1]), (sofa1[2], sofa1[3])]:
                for x2, y2 in [(sofa2[0], sofa2[1]), (sofa2[2], sofa2[3])]:
                    if y1 > y2:
                        right_found = True
                        break
                if right_found:
                    break
            if right_found:
                r_count += 1

            # Check top
            top_found = False
            for x1, y1 in [(sofa1[0], sofa1[1]), (sofa1[2], sofa1[3])]:
                for x2, y2 in [(sofa2[0], sofa2[1]), (sofa2[2], sofa2[3])]:
                    if x1 < x2:
                        top_found = True
                        break
                if top_found:
                    break
            if top_found:
                t_count += 1

            # Check bottom
            bottom_found = False
            for x1, y1 in [(sofa1[0], sofa1[1]), (sofa1[2], sofa1[3])]:
                for x2, y2 in [(sofa2[0], sofa2[1]), (sofa2[2], sofa2[3])]:
                    if x1 > x2:
                        bottom_found = True
                        break
                if bottom_found:
                    break
            if bottom_found:
                b_count += 1

        return l_count == cnt_l and r_count == cnt_r and t_count == cnt_t and b_count == cnt_b

    result = -1
    for i in range(d):
        if check_conditions(i):
            result = i + 1
            break

    print(result)

solve()