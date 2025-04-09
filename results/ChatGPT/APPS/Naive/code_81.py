def can_reorder_strings(strings):
    # Sort strings by length
    strings.sort(key=len)

    for i in range(len(strings)):
        for j in range(i):
            if strings[j] not in strings[i]:
                return "NO"

    return "YES", strings

def main():
    n = int(input())
    strings = [input().strip() for _ in range(n)]
    
    result = can_reorder_strings(strings)

    if result == "NO":
        print(result)
    else:
        print(result[0])
        for string in result[1]:
            print(string)

if __name__ == "__main__":
    main()