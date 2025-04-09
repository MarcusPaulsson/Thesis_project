def solve():
    ticket = input()
    
    min_replacements = 6
    
    for i in range(1000):
        for j in range(1000):
            first_three = str(i).zfill(3)
            last_three = str(j).zfill(3)
            
            new_ticket = first_three + last_three
            
            replacements = 0
            for k in range(6):
                if ticket[k] != new_ticket[k]:
                    replacements += 1
            
            if sum(int(digit) for digit in first_three) == sum(int(digit) for digit in last_three):
                min_replacements = min(min_replacements, replacements)
            
    print(min_replacements)

solve()