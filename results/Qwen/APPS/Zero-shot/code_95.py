def generate_string(n, s, t):
    if s == "aa" and t == "bb":
        return "NO"
    if s == "bb" and t == "aa":
        return "NO"
    if s == "ab" and t == "ba":
        return "NO"
    if s == "ba" and t == "ab":
        return "NO"
    if s == "ac" and t == "ca":
        return "NO"
    if s == "ca" and t == "ac":
        return "NO"
    if s == "bc" and t == "cb":
        return "NO"
    if s == "cb" and t == "bc":
        return "NO"
    
    res = ""
    for i in range(n):
        res += "a"
        if i < n - 1:
            res += "b"
        if i < n - 2:
            res += "c"
    
    return "YES", res

n = int(input())
s = input()
t = input()

result, res = generate_string(n, s, t)
print(result)
if result == "YES":
    print(res)