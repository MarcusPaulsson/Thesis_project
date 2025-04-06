from collections import Counter

def solve():
    a = input()
    b = input()

    a_counts = Counter(a)
    a_len = len(a)
    b_len = len(b)

    if a_len > b_len:
        print("".join(sorted(a, reverse=True)))
        return

    def find_max(index, current_num, remaining_counts):
        if index == a_len:
            return current_num
        
        best_num = ""

        for digit in sorted(remaining_counts.keys(), reverse=True):
            if remaining_counts[digit] > 0:
                temp_counts = remaining_counts.copy()
                temp_counts[digit] -= 1
                
                if temp_counts[digit] == 0:
                    del temp_counts[digit]
                
                new_num = current_num + digit
                
                if new_num <= b[:index+1]:
                    if new_num == b[:index+1]:
                        result = find_max(index+1, new_num, temp_counts)
                        if result:
                            if not best_num or result > best_num:
                                best_num = result
                    else:
                        remaining_digits = "".join(sorted(temp_counts.elements(), reverse=True))
                        result = new_num + remaining_digits
                        if not best_num or result > best_num:
                            best_num = result
        return best_num

    result = find_max(0, "", a_counts)
    print(result)

solve()