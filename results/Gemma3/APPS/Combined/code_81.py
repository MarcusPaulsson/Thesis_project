def solve():
    n = int(input())
    strings = []
    for _ in range(n):
        strings.append(input())

    def is_substring(s1, s2):
        return s1 in s2

    def find_order(current_order, remaining_strings):
        if not remaining_strings:
            return current_order

        for i in range(len(remaining_strings)):
            next_string = remaining_strings[i]
            valid = True
            for prev_string in current_order:
                if not is_substring(prev_string, next_string):
                    valid = False
                    break

            if valid:
                result = find_order(current_order + [next_string], remaining_strings[:i] + remaining_strings[i+1:])
                if result:
                    return result

        return None

    strings.sort(key=len)
    result = find_order([], strings)

    if result:
        print("YES")
        for s in result:
            print(s)
    else:
        print("NO")

solve()