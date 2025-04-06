def solve():
    n, k = map(int, input().split())
    t = input()

    def count_occurrences(s, target):
        count = 0
        for i in range(len(s) - len(target) + 1):
            if s[i:i + len(target)] == target:
                count += 1
        return count

    for length in range(n, n * k + 1):
        for start_index in range(0, 1):
            s = ""
            
            if start_index == 0:
              
                overlap = 0
                for i in range(1, n):
                    if t[:n-i] == t[i:]:
                        overlap = n - i
                        break
                        
                
                s = t
                num_needed = k - 1
                
                for _ in range(num_needed):
                  s += t[overlap:]

            
            if len(s) == length and count_occurrences(s, t) == k:
                print(s)
                return

solve()