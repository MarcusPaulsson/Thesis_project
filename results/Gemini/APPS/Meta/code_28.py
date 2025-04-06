def solve():
    n = int(input())
    files = []
    for _ in range(n):
        files.append(input().split())
    
    examples = []
    regular = []
    for i in range(n):
        if files[i][1] == '1':
            examples.append((files[i][0], i))
        else:
            regular.append((files[i][0], i))
            
    e = len(examples)
    
    moves = []
    
    # Move examples to 1, 2, ..., e
    for i in range(e):
        if examples[i][0] != str(i + 1):
            # Need to move examples[i][0] to i + 1
            
            # Check if i + 1 is already an example or regular
            found = False
            for j in range(n):
                if files[j][0] == str(i+1):
                    found = True
                    break
            
            if found:
                # Need a temporary move
                temp_name = "temp_" + str(i+1)
                
                while True:
                    found_temp = False
                    for j in range(n):
                        if files[j][0] == temp_name:
                            found_temp = True
                            break
                    if not found_temp:
                        break
                    temp_name = "temp_" + temp_name
                
                moves.append(f"move {files[i][0]} {temp_name}")
                files[examples[i][1]][0] = temp_name
                
                
                for k in range(n):
                    if files[k][0] == str(i+1):
                        moves.append(f"move {files[k][0]} {examples[i][0]}")
                        files[k][0] = examples[i][0]
                        break
                
                moves.append(f"move {temp_name} {str(i+1)}")
                files[examples[i][1]][0] = str(i+1)
                
            else:
                moves.append(f"move {files[i][0]} {str(i+1)}")
                files[examples[i][1]][0] = str(i+1)
                
    # Move regular tests to e+1, e+2, ..., n
    for i in range(len(regular)):
        if regular[i][0] != str(e + i + 1):
            # Need to move regular[i][0] to e + i + 1
            
            # Check if e + i + 1 is already an example or regular
            found = False
            for j in range(n):
                if files[j][0] == str(e + i + 1):
                    found = True
                    break
            
            if found:
                # Need a temporary move
                temp_name = "temp_" + str(e + i + 1)
                
                while True:
                    found_temp = False
                    for j in range(n):
                        if files[j][0] == temp_name:
                            found_temp = True
                            break
                    if not found_temp:
                        break
                    temp_name = "temp_" + temp_name
                
                moves.append(f"move {files[e + i][0]} {temp_name}")
                files[regular[i][1]][0] = temp_name
                
                for k in range(n):
                    if files[k][0] == str(e + i + 1):
                        moves.append(f"move {files[k][0]} {regular[i][0]}")
                        files[k][0] = regular[i][0]
                        break
                
                moves.append(f"move {temp_name} {str(e + i + 1)}")
                files[regular[i][1]][0] = str(e + i + 1)
            else:
                moves.append(f"move {files[e + i][0]} {str(e + i + 1)}")
                files[regular[i][1]][0] = str(e + i + 1)
    
    print(len(moves))
    for move in moves:
        print(move)
        
solve()