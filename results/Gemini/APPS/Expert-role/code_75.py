def solve():
    a, b, c = map(int, input().split())
    
    days = [
        [0, 1, 2, 0, 2, 1, 0],
        [1, 2, 0, 2, 1, 0, 0],
        [2, 0, 2, 1, 0, 0, 1],
        [0, 2, 1, 0, 0, 1, 2],
        [2, 1, 0, 0, 1, 2, 0],
        [1, 0, 0, 1, 2, 0, 2],
        [0, 0, 1, 2, 0, 2, 1]
    ]
    
    max_days = 0
    for start_day in range(7):
        curr_a, curr_b, curr_c = a, b, c
        curr_days = 0
        
        while True:
            possible = True
            for i in range(7):
                food_type = days[start_day][i]
                
                if food_type == 0:
                    if curr_a > 0:
                        curr_a -= 1
                        curr_days += 1
                    else:
                        possible = False
                        break
                elif food_type == 1:
                    if curr_b > 0:
                        curr_b -= 1
                        curr_days += 1
                    else:
                        possible = False
                        break
                else:
                    if curr_c > 0:
                        curr_c -= 1
                        curr_days += 1
                    else:
                        possible = False
                        break
            
            if not possible:
                break
            
            
            
            week_days = 0
            temp_a, temp_b, temp_c = a, b, c
            
            week_possible = True
            for i in range(7):
                food_type = days[start_day][i]
                if food_type == 0:
                    if temp_a > 0:
                        temp_a -= 1
                        week_days += 1
                    else:
                        week_possible = False
                        break
                elif food_type == 1:
                    if temp_b > 0:
                        temp_b -= 1
                        week_days += 1
                    else:
                        week_possible = False
                        break
                else:
                    if temp_c > 0:
                        temp_c -= 1
                        week_days += 1
                    else:
                        week_possible = False
                        break
            
            if week_possible:
                
                num_weeks = min(curr_a // (a - temp_a), curr_b // (b - temp_b) if (b - temp_b) != 0 else float('inf'), curr_c // (c - temp_c) if (c - temp_c) != 0 else float('inf'))
                
                
                
                if num_weeks > 0:
                    curr_days += num_weeks * 7
                    curr_a -= num_weeks * (a - temp_a)
                    curr_b -= num_weeks * (b - temp_b)
                    curr_c -= num_weeks * (c - temp_c)

                else:
                    
                    temp_days = 0 
                    loop_possible = True
                    
                    for i in range(7):

                        food_type = days[start_day][i]


                        if food_type == 0:
                            if curr_a > 0:
                                curr_a -= 1
                                curr_days += 1
                                temp_days +=1
                            else:
                                loop_possible = False
                                break
                        elif food_type == 1:
                            if curr_b > 0:
                                curr_b -= 1
                                curr_days += 1
                                temp_days +=1
                            else:
                                loop_possible = False
                                break
                        else:
                            if curr_c > 0:
                                curr_c -= 1
                                curr_days += 1
                                temp_days +=1
                            else:
                                loop_possible = False
                                break

                    if not loop_possible:
                        break
                
            else:
                break


        max_days = max(max_days, curr_days)
    
    print(max_days)
    
solve()