def is_valid_result(res, s, t):
    return not (s in res or t in res)

def add_char(res, char, last_chars):
    if res and res[-1] == char:
        return False
    if len(res) >= 2 and (res[-1] == last_chars[0] and res[-2] == last_chars[1]):
        return False
    res.append(char)
    return True

def build_result(n, s, t):
    a_count = b_count = c_count = n
    res = []

    while a_count > 0 or b_count > 0 or c_count > 0:
        if a_count > 0 and add_char(res, 'a', (s[0], t[0])):
            a_count -= 1
        elif b_count > 0 and add_char(res, 'b', (s[0], t[0])):
            b_count -= 1
        elif c_count > 0 and add_char(res, 'c', (s[0], t[0])):
            c_count -= 1
        else:
            return "NO", ""

    result_str = ''.join(res)
    return ("NO", "") if not is_valid_result(result_str, s, t) else ("YES", result_str)

n = int(input())
s = input().strip()
t = input().strip()

result = build_result(n, s, t)
if result[0] == "NO":
    print("NO")
else:
    print("YES")
    print(result[1])