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
            
    moves = []
    
    e = len(examples)
    
    # Move examples to 1, 2, ..., e
    for i in range(e):
        if examples[i][0] != str(i + 1):
            
            # If there's a collision with a target filename, move it to a temp name
            if any(f[0] == str(i+1) for f in files):
                
                 #find the file that has the name str(i+1) and its index
                colliding_file_index = next(index for index, file in enumerate(files) if file[0] == str(i+1))
                
                temp_name = "temp" + str(i+1)
                while any(f[0] == temp_name for f in files):
                    temp_name = "temp" + temp_name
                
                moves.append(f"move {str(i+1)} {temp_name}")
                files[colliding_file_index][0] = temp_name
                
                
            moves.append(f"move {examples[i][0]} {str(i + 1)}")
            files[examples[i][1]][0] = str(i+1)
            
            
    # Move regular tests to e+1, e+2, ..., n
    for i in range(len(regular)):
        if regular[i][0] != str(e + i + 1):
            
            # If there's a collision with a target filename, move it to a temp name
            if any(f[0] == str(e+i+1) for f in files):
                #find the file that has the name str(e+i+1) and its index
                colliding_file_index = next(index for index, file in enumerate(files) if file[0] == str(e+i+1))
                
                temp_name = "temp" + str(e+i+1)
                while any(f[0] == temp_name for f in files):
                    temp_name = "temp" + temp_name
                
                moves.append(f"move {str(e+i+1)} {temp_name}")
                files[colliding_file_index][0] = temp_name
            
            
            moves.append(f"move {regular[i][0]} {str(e + i + 1)}")
            files[regular[i][1]][0] = str(e+i+1)
    
    print(len(moves))
    for move in moves:
        print(move)

solve()