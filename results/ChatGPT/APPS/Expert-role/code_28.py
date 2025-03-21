def can_form_abacaba(s):
    abacaba = "abacaba"
    n = len(s)

    # Check how many times "abacaba" can fit in the string
    count = 0
    for i in range(n - 6):
        if all(s[i + j] == abacaba[j] or s[i + j] == '?' for j in range(7)):
            count += 1

    return count

def replace_question_marks(s, position):
    abacaba = "abacaba"
    result = list(s)
    
    for i in range(len(result)):
        if i >= position and i < position + 7:
            result[i] = abacaba[i - position]
        elif result[i] == '?':
            result[i] = 'z'  # Replace with any letter that doesn't affect abacaba
            
    return ''.join(result)

def process_test_cases(test_cases):
    results = []
    for s in test_cases:
        n = len(s)
        
        # First, we check how many occurrences can be made
        count = can_form_abacaba(s)

        if count > 1:
            results.append("No")
            continue

        # Try to place "abacaba" in each possible position
        found = False
        for i in range(n - 6):
            if all(s[i + j] == 'abacaba'[j] or s[i + j] == '?' for j in range(7)):
                # Create a new string with "abacaba" placed here
                new_string = replace_question_marks(s, i)
                if can_form_abacaba(new_string) == 1:
                    results.append("Yes")
                    results.append(new_string)
                    found = True
                    break
        
        if not found:
            results.append("No")
    
    return results

# Input reading
T = int(input())
test_cases = [input().strip() for _ in range(2 * T)]
results = process_test_cases(test_cases[1::2])

# Output results
for result in results:
    print(result)