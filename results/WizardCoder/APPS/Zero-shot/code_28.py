import itertools

def is_valid(s):
    # check if there is exactly one occurrence of "abacaba" as a substring
    return s.count("abacaba") == 1


# read input T, test cases and loop through them
T = int(input())
for i in range(T):
    n = int(input())
    s = input()
    if is_valid(s):
        print("Yes")
        # generate all possible combinations of letters for question marks and check each one
        for perm in itertools.product('abcdefghijklmnopqrstuvwxyz', repeat=s.count('?')):
            t = ''
            j = 0
            k = 0
            while j < len(s):
                if s[j] == '?':
                    t += perm[k]
                    k += 1
                else:
                    t += s[j]
                j += 1
            if is_valid(t):
                print(t)
                break
    else:
        print("No")