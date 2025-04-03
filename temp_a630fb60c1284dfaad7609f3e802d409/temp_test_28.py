def solve():
    n = int(input())
    s = input()
    target = "abacaba"
    
    def count_occurrences(text):
        count = 0
        for i in range(len(text) - len(target) + 1):
            if text[i:i+len(target)] == target:
                count += 1
        return count

    def replace_and_check(start_index):
        temp_s = list(s)
        
        for i in range(len(target)):
            if temp_s[start_index + i] == '?':
                temp_s[start_index + i] = target[i]
            elif temp_s[start_index + i] != target[i]:
                return None
        
        result_s = "".join(temp_s)
        
        final_s = list(result_s)
        for i in range(len(final_s)):
            if final_s[i] == '?':
                final_s[i] = 'd'
        
        final_str = "".join(final_s)
        
        if count_occurrences(final_str) == 1:
            return final_str
        else:
            return None

    for i in range(n - len(target) + 1):
        result = replace_and_check(i)
        if result:
            print("Yes")
            print(result)
            return

    print("No")


t = int(input())
for _ in range(t):
    solve()