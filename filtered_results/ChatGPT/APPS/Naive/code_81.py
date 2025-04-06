def can_reorder_strings(n, strings):
    # Sort strings by their lengths
    strings.sort(key=len)
    
    # Check if each string is a substring of the next one
    for i in range(n - 1):
        if strings[i] not in strings[i + 1]:
            return False, []
    
    return True, strings

def main():
    n = int(input().strip())
    strings = [input().strip() for _ in range(n)]
    
    possible, reordered_strings = can_reorder_strings(n, strings)
    
    if possible:
        print("YES")
        for s in reordered_strings:
            print(s)
    else:
        print("NO")

if __name__ == "__main__":
    main()